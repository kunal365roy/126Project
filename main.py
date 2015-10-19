# -*- coding: utf-8 -*-
import re
import sys
import urllib
import urlparse
import random
from bs4 import BeautifulSoup
from collections import Counter
from collections import namedtuple

TeamRegexTuple = namedtuple('TeamRegexTuple', ['city', 'teamname'])

#http://wolfprojects.altervista.org/articles/change-urllib-user-agent/ 

class MyOpener(urllib.FancyURLopener):
   version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'

#This function will parse a url to give you the domain. Test it!
def domain(url):
    #urlparse breaks down the url passed it, and you split the hostname up 
    #Ex: hostname="www.google.com" becomes ['www', 'google', 'com']
    hostname = urlparse.urlparse(url).hostname.split(".")
    hostname = ".".join(len(hostname[-2]) < 4 and hostname[-3:] or hostname[-2:])
    return hostname
    
#This function will return all the urls on a page, and return the start url if there is an error or no urls
def parse_links(url, url_start):
    url_list = []
    myopener = MyOpener()
    try:
        #open, read, and parse the text using beautiful soup
        page = myopener.open(url)
        text = page.read()
        page.close()
        soup = BeautifulSoup(text, "lxml")

        #find all hyperlinks using beautiful soup
        for tag in soup.findAll('a', href=True):
            #concatenate the base url with the path from the hyperlink
            tmp = urlparse.urljoin(url, tag['href'])
            #we want to stay in the berkeley domain. This becomes more relevant later
            if domain(tmp).endswith('berkeley.edu'):
                url_list.append(tmp)
        if len(url_list) == 0:
            return [url_start]
        return url_list
    except:
        return [url_start]

def generate_teams_regex (file_path):

    '''
    Generates team and city name regexes from a structured file
    
    File should be structured like
    Seattle Seahawks
    San Francisco 49ers

    (i.e. city name with an arbitrary number of words,
        team name as the last word)

    '''
    
    team_names = []
    teams_regex = {}
    with open(file_path, 'r') as teams:
        lines = teams.readlines()
        for line in lines:
            data = line.strip('\n').split()
            name = data[-1]
            city = ' '.join(data[0:-1])
            city_pre_regex = '{0}|{1}'.format(city, city.upper)

            regex_list = TeamRegexTuple(re.compile(city_pre_regex), re.compile(name))
            team_names.append(name)
            teams_regex[name] = regex_list

    return team_names, teams_regex

def count_team_mentions (target_url, teams_regex):
    '''
    Only goes through the paragraph tags, so we don't get
        confused by scores listed in sidebars and menu bars
        and other similar junk

    The intent is to consider only the content of the article

    @param target_url - url of the article page that we want to count
    @param teams_regex - dictionary containing teams and their associated regexes
    '''

    opener = MyOpener()
    page = opener.open(target_url)
    text = page.read()
    page.close()


    mention_counter = Counter()

    soup = BeautifulSoup(text)
    paragraph_nodes = map(str, soup.findAll('p'))

    mention_counter = Counter()

    # first need to figure out which teams are worth looking at.
    # want city and team name to appear at least once each in the same article
    # this way if we click on a baseball link for the St. Louis Cardinals
    #   we won't start capturing data for the NFL Arizona Cardinals
    useful_teams = []
    for team_name, team_regexes in teams_regex.items():
        city_regex = team_regexes.city
        name_regex = team_regexes.teamname

        contains_city_regex, contains_name_regex = False, False
        for paragraph in paragraph_nodes:
            contains_city_regex = contains_city_regex or \
                        (len(re.findall(city_regex, paragraph)) != 0)
            contains_name_regex = contains_name_regex or \
                        (len(re.findall(name_regex, paragraph)) != 0)

            if contains_city_regex and contains_name_regex:
                break

        if contains_city_regex and contains_name_regex:
            useful_teams.append(team_name)

    for paragraph in paragraph_nodes:
        for team_name in useful_teams:
            for regex in teams_regex[team_name]:
                match_count = len(re.findall(regex, paragraph))
                mention_counter[team_name] += match_count

    return mention_counter

url_start = "http://www.eecs.berkeley.edu/Research/"
current_url = url_start
num_of_visits = 200

#List of professors obtained from the EECS page
profs = ['Abbeel','Agrawala','Alon','Anantharam','Arcak','Arias','Asanović','Bachrach','Bajcsy','Bodik','Bokor','Boser','Brewer','Canny','Chang-Hasnain','Culler','Darrell','Demmel','Fearing','Fox','Franklin','Garcia','Goldberg','Hartmann','Harvey','Hellerstein','Javey','Joseph','Katz','Keutzer','Liu','Klein','Kubiatowicz','Lee','Lustig','Maharbiz','Malik','Nguyen','Niknejad','Nikolic',"O'Brien",'Parekh','Patterson','Paxson','Pisano','Rabaey','Ramchandran','Roychowdhury','Russell','Sahai','Salahuddin','Sanders','Sangiovanni-Vincentelli','Sastry','Sen','Seshia','Shenker','Song','Song','Spanos','Stoica','Stojanovic','Tomlin','Tygar','Walrand','Wawrzynek','Wu','Yablonovitch','Yelick','Zakhor']
#Bad URLs help take care of some pathologies that ruin our surfing
bad_urls = ['http://www.erso.berkeley.edu/','http://www.eecs.berkeley.edu/Rosters/roster.name.nostudentee.html','http://www.eecs.berkeley.edu/Resguide/admin.shtml#aliases','http://www.eecs.berkeley.edu/department/EECSbrochure/c1-s3.html']

#Creating a dictionary to keep track of how often we come across a professor
profdict = {}
for i in profs:
    profdict[i] = 0

for i in range(num_of_visits):
    print  i , ' Visiting... ', current_url
    if random.random() < 0.95: #follow a link!
        url_list = parse_links(current_url, url_start)
        updated = False
        while not updated:
            current_url = random.choice(url_list)
            updated = True
            if current_url in bad_urls or "iris" in current_url or "Deptonly" in current_url or "anchor" in current_url or "erso" in current_url: #dealing with more pathologies:
                updated = False
        myopener = MyOpener()
        page = myopener.open(current_url)
        text = page.read()
        page.close()
        #Figuring out which professor is mentioned on a page.
        for p in profs:
            profdict[p]+= 1 if " " + p + " " in text else 0 #can use regex re.findall(i,text), but it's overkill
    else: #click the "home" button!
        current_url = url_start
