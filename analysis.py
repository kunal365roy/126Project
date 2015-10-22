from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
from collections import namedtuple
import matplotlib as matplotlib
from scipy.interpolate import interp1d
import pylab

sentiment_dict = {'Raiders': 21.152994227994224, 'Vikings': 12.061819727891152, 'Bears': 1.7292424242424245, 'Falcons': 7.9099623788909605, 'Saints': 13.407335700014283, 'Chargers': 8.262153725903726, 'Broncos': 16.386266835016833, 'Lions': 3.0486774891774884, 'Browns': 4.22175925925926, 'Eagles': 32.695626503126654, 'Steelers': 46.68501082251084, 'Giants': 101.23723965848971, 'Cardinals': 0.3275757575757573, 'Bengals': 8.735331890331892, 'Chiefs': 2.0150324675324693, 'Jaguars': 16.740515873015873, 'Seahawks': 0.7333333333333334, 'Jets': 119.8964303751804, 'Ravens': 2.241666666666667, 'Packers': 0.6909090909090909, 'Dolphins': 1.5617424242424238, 'Titans': 1.8636832611832606, 'Bucaneers': 0.8970833333333329, 'Rams': 90.69593795093793, 'Bills': 7.266349206349207, 'Texans': 4.0654070466570404, '49ers': 24.249312770562767, 'Patriots': 104.75590668590675, 'Cowboys': 40.515680014429996, 'Panthers': 5.898134920634919, 'Redskins': 6.58284857503607}

popularity_dict = {'Raiders': 18.179643619993897, 'Vikings': 13.910204145264553, 'Bears': 8.979466578731286, 'Falcons': 10.252223518136496, 'Saints': 17.6541525503482, 'Chargers': 9.539374946468138, 'Broncos': 11.55691352543714, 'Lions': 17.274479097628358, 'Browns': 12.4812235827301, 'Eagles': 38.868260831453014, 'Steelers': 17.996639552801984, 'Giants': 40.562848128545255, 'Buccaneers': 8.541381157167166, 'Cardinals': 28.39657182302996, 'Bengals': 6.630018062442437, 'Chiefs': 9.149365356687603, 'Jaguars': 30.554838483936624, 'Seahawks': 15.710811888076673, 'Jets': 46.01819764679456, 'Ravens': 15.286902759587557, 'Colts': 7.485321417798866, 'Packers': 12.93272028276539, 'Dolphins': 21.40710629606611, 'Rams': 19.94264139665947, 'Bills': 11.388976353833876, 'Panthers': 12.610628947819519, 'Texans': 28.435517568117305, '49ers': 17.392488445392136, 'Patriots': 49.02131590955723, 'Cowboys': 30.56018227572322, 'Titans': 18.21346971149202, 'Redskins': 14.06611413951378}

if __name__ == '__main__':
    sentiments_vector = []
    popularity_vector = []
    team_vector = []

    for (team_name1, sentiment), (team_name2, popularity) in zip(sentiment_dict.items(), popularity_dict.items()):
        sentiments_vector.append(sentiment)
        popularity_vector.append(popularity)
        team_vector.append(team_name1)


    pp = PdfPages('sentiment_v_popularity.pdf')
    fig, ax = plt.subplots()

    thing = plt.scatter(popularity_vector, sentiments_vector, 
                    color='#000000')

    interesting_teams = set(['Jets', 'Patriots', 'Giants', 'Steelers', 'Rams', '49ers', 'Bills'])
    for label, x, y in zip(team_vector, popularity_vector, sentiments_vector):
        if label in interesting_teams:
            plt.annotate(
                label, 
                xy = (x, y), xytext = (30, 20),
                textcoords = 'offset points', ha = 'right', va = 'bottom',
                bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
                arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

    plt.ylabel("Sentiment score")
    plt.xlabel("Popularity score")
    plt.title("Sentiment vs. popularity")

    pp.savefig()
    pp.close()



