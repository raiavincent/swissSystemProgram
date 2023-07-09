import random


# find tournament length
# force number
while True:
    try:
        rounds = int(input('Enter desired number of rounds: '))
        break
    except ValueError:
        print('Enter a number')
        continue

# take input of player names
# create an empty list of players at the start, that can take any number of inputs

playerList = []

while True:
    player = input("Enter player name, if done, input 'exit': ")
    if player.lower() == 'exit':
        break
    else:
        playerList.append(player)

print(playerList)

# need a way to keep scores
# create a dicitionary with all keys = 0

scoresInit = {key: 0  for key in playerList}

print(scoresInit)

# pair players
# for the first round, random numbers for pairing, add to a list of lists

pairList = []

while len(playerList) > 0:
    for player in playerList:
        pair = random.sample(range(len(playerList)),2)
        print(pair)
        pairing = [playerList[pair[0]],playerList[pair[1]]]
        print(pairing)
        if all(x in pairList for x in pairing):
            pairList.append([playerList[pair[0]],playerList[pair[1]]])
            playerList = [x for x in playerList if x not in pairing]
            print('Pairlist:' + pairList)
        else:
            pass



print(pairList)
print(playerList)