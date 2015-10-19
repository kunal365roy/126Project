from textblob import TextBlob
from collections import Counter

text = '''
NASHVILLE, Tenn. -- Titans coach Ken Whisenhunt and left tackle Taylor Lewan had strong words for Dolphins defensive end Olivier Vernon's hit on Marcus Mariota in the first quarter of Sunday's game.

"I think it was B.S.," Whisenhunt said after Tennessee's 38-10 loss to Miami. "That's not the way you play football. I think it was done with the idea of trying to hurt our quarterback, and that's bulls--- football."
Mariota didn't leave the game, but he was clearly hobbled and wore a left knee brace for the remainder of the game, in which he lost two fumbles and threw two interceptions.
The rookie quarterback said Vernon approached him after the game to apologize for the play, which drew a roughing the passer flag.
EDITOR'S PICKS
While protection and weapons were poor, so was Marcus Mariota
Titans' rookie QB Marcus Mariota needs to find a way to bring out the best of his offensive line and receivers instead of letting them pull him down.
Marcus Mariota plays through left knee injury
A hit to the knee wasn't enough to sideline Marcus Mariota, but he struggled in the first half.
With sliver of a fourth-quarter chance, Titans blow it, get blown out
"I don't think it was malicious," Mariota said.

Vernon acknowledged that he wanted to see video replay of the hit but emphasized that he is not "a dirty player."
"I know one thing -- it wasn't intentional," Vernon said. "I've never been a dirty player in my whole career. ... Nobody tries to get personal fouls. I know one thing, they are expensive."

Mariota said he expects to be a full-go for Wednesday's practice as the Titans prepare for next week's home game against Atlanta. He was sacked five times Sunday, raising his season total to 19.
Despite Mariota's sentiment, Lewan echoed Whisenhunt's criticism of Vernon's hit.

"I think it is bulls--- football," said Lewan, who was beaten by Vernon on the play. "I'm so tired of people being politically correct. That's bulls---, that's f---ing bulls--- to do that to a player -- to do that to a guy's career.

"That was my guy and I blocked him, and Marcus threw the ball and I saw Marcus threw the ball, and that guy jumped in his legs. Do I wish anything upon him? No. I should have blocked him longer. That's the end of the story."
'''

text2= '''

PITTSBURGH -- Steelers quarterback Landry Jones replaced a struggling Mike Vick and gave Pittsburgh's offense new life, throwing two touchdown passes to Martavis Bryant in Sunday's 25-13 victory over the Cardinals.

Vick, who was evaluated for a hamstring injury, has not played well since taking over for an injured Ben Roethlisberger in Week 3, throwing for less than 300 yards in his past 10 quarters of play, including a 3-of-8 performance for 6 yards in two-plus quarters Sunday.

EDITOR'S PICKS
Fowler: Steelers are legit SB contenders
The Steelers are Super Bowl contenders. Don't forget it now, don't forget it when Ben Roethlisberger returns as early as next week, Jeremy Fowler writes.
Jones impressed his offensive teammates, including star running back Le'Veon Bell, who noticed Jones calling audibles at the line of scrimmage as if he had been doing it for years.

"It was really like Ben's little brother out there," Bell said. "It kind of brought us back like, 'Dang, Landry has really got this.'"

"That's something he's been working tirelessly for," Steelers coach Mike Tomlin added.

As for next week's starter at Kansas City, Tomlin made no promises but acknowledged "we've got some options." Tomlin isn't sure of the severity of Vick's hamstring injury.

Jones' early-third-quarter score gave the Steelers a 12-10 lead. Jones threw the ball hard and high for a soaring Bryant, who barely kept his body in bounds.

Jones and Bryant hooked up for a touchdown again in the fourth quarter, an 88-yard scoring strike that gave Pittsburgh a 25-13 lead with two minutes remaining. It was the longest play from scrimmage in the NFL this season.

Jones finished 8-of-12 for 168 yards, while Bryant, who was making his season debut after serving a four-game suspension, had six catches for 137 yards.

Jones briefly stepped in during the first half while Vick went to the sideline with dirt in his eye, but the second-half marks the first extended NFL action from the 2013 fourth-round pick. Jones struggled for parts of training camp, so his continued presence on the field is hardly a sure thing.
'''


text3= '''
CLEVELAND -- Again far from perfect, Peyton Manning still kept Denver's record pristine.

Manning shook off three interceptions, including one early in overtime, and drove Denver's offense in range for Brandon McManus to kick a 34-yard field goal with 4:56 left, giving the unbeaten Broncos a 26-23 win over the Cleveland Browns on Sunday.

Manning took the Broncos from their 12 to the Cleveland 16 before McManus kicked his game-winner to make Denver 6-0 for the seventh time in franchise history.

"We're not playing as well as we would like but we're playing well enough to win," Manning said. "We're doing some things right at critical times whether it's the last drive of the game or in overtime."

EDITOR'S PICKS
History says 6-0 start usually means Super Bowl trip for Broncos
The Broncos are 6-0, which is the seventh time in franchise history they have started a season 6-0. On five of the other occasions (1977, 1986, 1997, 1998 and 2013) the Broncos advanced to the Super Bowl.

Stats: It's not going good for the Broncos, but not for 
The Broncos quarterback has already matched his interception total from 2013, but he has only seven touchdown passes. We review his struggles.

Browns focus on game, not Manziel incident
The Browns said very little about Johnny Manziel being questioned by Avon, Ohio, police following an argument in his car with his girlfriend last Monday as the team preferred to focus on the loss to Denver, Pat McManamon writes.
Denver's win would not have been possible without the Broncos' top-ranked defense, which came up huge in overtime and has carried the team -- and the 39-year-old Manning -- during the club's unblemished start.

After Manning's third pick, Denver recorded a tackle behind the line of scrimmage and then had two consecutive sacks of Josh McCown to push the Browns (2-4) out of field-goal range.

"Obviously that's not a good situation to put the defense in, but they got a couple of sacks and gave us a chance," said Manning, who has seven TD passes and 10 interceptions this season. "I'm not having a ton of breaks. I won't be going to Vegas for my bye week. I'm not feeling really lucky."

But Denver's defense bailed him out, and given another chance in overtime, Manning took over. He completed 4 of 4 passes for 39 yards on the last drive. Manning finished 26 of 48 for 290 yards and the one TD, a 75-yarder to Emmanuel Sanders.

The score came just seconds after the Browns had taken their only lead on Karlos Dansby's 35-yard interception return for a TD.

It was yet another heartbreaker for Cleveland, which had one of the NFL's best teams on the ropes late in regulation before McCown threw a critical interception.

McCown, who passed for a franchise-record 457 yards last week, went 20 of 39 for 213 yards with two touchdowns to tight end Gary Barnidge. But his second pick with 44 seconds left in regulation cost the Browns as they were driving for a potential game-winning field goal.

On second down at the Denver 46, McCown rolled from pressure before forcing a throw across the field that was picked off by Denver's David Bruton Jr.

"It was obviously just not good," McCown said of his turnover. "You have to get something going there. That hurt us because the defense played lights-out today. We didn't hold up our end. It is a shame."

Denver cornerback Aqib Talib had a 63-yard interception return for a TD and McManus kicked four field goals as the Broncos won their 11th straight against the Browns.

This one didn't have much artistic beauty as the Broncos had some dropped passes, penalties and let the Browns hang around.

But Manning, as he has done so many times during his illustrious career, found a way to lead his team to the win. His struggles have prompted talk about his career reaching an end, but Denver, relying on its swarming, turnover-inducing defense, is winning without Manning playing well.

"We're a good football team that could be a great football team, if we can correct a lot of our mistakes," Broncos coach Gary Kubiak said.

The overtime came after a frenetic fourth quarter during which Cleveland took the lead on Dansby's interception -- off a pass bobbled by Denver's Ronnie Hillman -- only to have Manning take it back 14 seconds later with his strike to Sanders.

Denver's dominating defense, missing injured linebacker DeMarcus Ware, came up with another big play in the first half as Talib's return gave the Broncos a 10-0 lead.

On the second play of the second quarter, McCown threw a pass toward the right sideline, where Talib was waiting. He made the interception, and after briefly holding the ball out in an early celebration, tucked it away and outran Travis Benjamin to the end zone.

It was Denver's fourth defensive TD this season and the eighth of Talib's career.

Hillman rushed for 111 yards on 20 carries. Demaryius Thomas had 10 catches for 111 yards, but let two clutch throws by Manning slip through his hands.

Game notes
Denver is 4-0 in road games. ... Already missing Ware (back), the Broncos also lost LBs Shane Ray (knee) and Corey Nelson (knee). Ray's injury appears to be the most serious. He left the stadium on crutches and his knee immobilized. ... Sanders hurt his left shoulder while making a catch late in regulation. ... Barnidge is the first Browns TE to catch a TD pass in four straight games since Ozzie Newsome in 1981.
'''

text4 = 'Broncos not amazing'
print TextBlob(text4).sentences[0].sentiment


# Remove non ascii characters 
def non_ascii(text):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])

# Returns counter with sentiment for each team
def get_sentiment(text):
    blob = TextBlob(non_ascii(text))
    blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]
  
    TeamCounter= Counter({
             ("Seattle","Seahawks"):0,
             ("San Francisco","49ers"):0,
             ("St. Louis", "Rams"):0,
             ("Arizona", "Cardinals"):0,
             ("Chicago","Bears"):0,
             ("Green Bay","Packers"):0,
             ("Minnesota","Vikings"):0,
             ("Detroit","Lions"):0,
             ("Philadelphia","Eagles"):0,
             ("Dallas","Cowboys"):0,
             ("New York","Giants"):0,
             ("Washington","Redskins"):0,
             ("Tampa Bay","Bucaneers"):0,
             ("New Orleans","Saints"):0,
             ("Atlanta","Falcons"):0,
             ("Carolina","Panthers"):0,
             ("Denver","Broncos"):0,
             ("San Diego","Chargers"):0,
             ("Kansas City","Chiefs"):0,
             ("Oakland","Raiders"):0,
             ("Pittsburgh","Steelers"):0,
             ("Baltimore","Ravens"):0,
             ("Cleveland","Browns"):0,
             ("Cincinatti","Bengals"):0,
             ("New England","Patriots"):0,
             ("Miami","Dolphins"):0, 
             ("Buffalo","Bills"):0,
             ("New York","Jets"):0,
             ("Indianappolis","Colts"):0,
             ("Jacksonville","Jaguars"):0,
             ("Houston","Texans"):0,
             ("Tennesee","Titans"):0,
             })

    # check each 
    for sentence in blob.sentences:
        for key in TeamCounter: 
            for name in key:
                if name in sentence:
                    TeamCounter[key]+=sentence.sentiment.polarity
                    continue #don't double count itmes
    return TeamCounter
