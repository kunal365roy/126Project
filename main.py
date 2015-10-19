# -*- coding: utf-8 -*-
import re
import sys
import urllib
import urlparse
import random
from bs4 import BeautifulSoup
import sentiment

#http://wolfprojects.altervista.org/articles/change-urllib-user-agent/ 
num_of_visits = 200

print('Starting espn pagerank with ' + str(num_of_visits) + ' visits.')


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
            if isValidUrl(tmp):
                url_list.append(tmp)
        if len(url_list) == 0:
            return [url_start]
        return url_list
    except:
        return [url_start]

def isValidUrl(url):
    base_urls = ['http://espn.go.com/nfl/', 'http://espn.go.com/blog/']
    for base_url in base_urls:
        if url.startsWith(base_url):
            return True
    return False

url_start = "http://espn.go.com/nfl"
current_url = url_start

#Bad URLs help take care of some pathologies that ruin our surfing
#Creating a dictionary to keep track of how often we come across a professor
teamsdict = {}

for i in range(num_of_visits):
    print  i , ' Visiting... ', current_url
    if random.random() < 0.95: #follow a link!
        url_list = parse_links(current_url, url_start)
        myopener = MyOpener()
        page = myopener.open(current_url)
        text = page.read()
        page.close()
        #Figuring out which professor is mentioned on a page.
        for team in teamsdict:
            teamsdict[team]+= 1 if " " + p + " " in text else 0 #can use regex re.findall(i,text), but it's overkill
    else: #click the "home" button!
        current_url = url_start