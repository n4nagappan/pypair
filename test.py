#A simple script for testing pypair

from pypair import Tournament
import random
import os
import sys
import json

home = os.path.expanduser("~")

to = Tournament()

#for p in range(10):
#    to.addPlayer( p, "Timmy" )

def disp():
    x = sorted(to.playersDict.values(), reverse=True, key=lambda x: x["Points"])
    for player in x:
        print('---------------------')
        print( player['Name'])
        print( "Points : ", player['Points'])
        print( "Opponents", )
        for opponent in player['Opponents']:
            if opponent != 'bye':
                print("\t", to.playersDict[opponent]['Name'])
            else:
                print("\t", 'BYE')
        print( "Results", )
        for result in player['Results']:
            print("\t", result)

to.loadPlayersCSV("playerlist.csv")
print("")
disp()
print("+++")

pairings1 = to.pairRound()

print("Pairings 1")
print(pairings1)

for table in pairings1:
    if not type(pairings1[table]) is str:
        per = random.randint(1, 100)
        if per < 33:
            to.reportMatch(table, [2,0,0])
        elif per < 66:
            to.reportMatch(table, [0,2,0])
        else:
            to.reportMatch(table, [1,1,0])

print("Saving")
to.saveEventData("/tmp/datadump1.txt")
to.loadEventData("/tmp/datadump1.txt")
print("Loading")

print("")
disp()
print("---")

sys.exit()

pairings2 = to.pairRound()

print(pairings2)

for table in pairings2:
    if not type(pairings2[table]) is str:
        per = random.randint(1, 100)
        if per < 33:
            to.reportMatch(table, [2,0,0])
        elif per < 66:
            to.reportMatch(table, [0,2,0])
        else:
            to.reportMatch(table, [1,1,0])

to.saveEventData("%s/datadump2.txt"%home)

print("")
#print to.playersDict[256]
disp()
print("")

pairings3 = to.pairRound()

print(pairings3)

for table in pairings3:
    if not type(pairings3[table]) is str:
        per = random.randint(1, 100)
        if per < 33:
            to.reportMatch(table, [2,0,0])
        elif per < 66:
            to.reportMatch(table, [0,2,0])
        else:
            to.reportMatch(table, [1,1,0])

to.saveEventData("%s/datadump3.txt"%home)

print("")
#print to.playersDict[256]
disp()
print("")

pairings4 = to.pairRound()

print(pairings4)

for table in pairings4:
    if not type(pairings4[table]) is str:
        per = random.randint(1, 100)
        if per < 33:
            to.reportMatch(table, [2,0,0])
        elif per < 66:
            to.reportMatch(table, [0,2,0])
        else:
            to.reportMatch(table, [1,1,0])

to.saveEventData("%s/datadump4.txt"%home)

print("")
# print(to.playersDict[256])
disp()
print("")

pairings5 = to.pairRound()

print(pairings5)

for table in pairings5:
    if not type(pairings5[table]) is str:
        per = random.randint(1, 100)
        if per < 33:
            to.reportMatch(table, [2,0,0])
        elif per < 66:
            to.reportMatch(table, [0,2,0])
        else:
            to.reportMatch(table, [1,1,0])

to.saveEventData("%s/datadump5.txt"%home)

print("")
# print(to.playersDict[256])
disp()
print("")


