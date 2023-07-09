
# find tournament length
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