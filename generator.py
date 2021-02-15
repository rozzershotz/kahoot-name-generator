import random
print ('''
 /$$   /$$ /$$$$$$$$ /$$       /$$        /$$$$$$  /$$ /$$ /$$ /$$
| $$  | $$| $$_____/| $$      | $$       /$$__  $$| $$| $$| $$| $$
| $$  | $$| $$      | $$      | $$      | $$  \ $$| $$| $$| $$| $$
| $$$$$$$$| $$$$$   | $$      | $$      | $$  | $$| $$| $$| $$| $$
| $$__  $$| $$__/   | $$      | $$      | $$  | $$|__/|__/|__/|__/
| $$  | $$| $$      | $$      | $$      | $$  | $$                
| $$  | $$| $$$$$$$$| $$$$$$$$| $$$$$$$$|  $$$$$$/ /$$ /$$ /$$ /$$
|__/  |__/|________/|________/|________/ \______/ |__/|__/|__/|__/
                                                               
''')

class Player:
    def PrintName(self):
        print(self.name)
    def PrintNameAndScore(self):
        print(self.name + " --> " + str(self.score))
    name = ""
    score = 0

def GetNumberFromUser(message, errormessage):
    ValidInputGiven = False
    while ValidInputGiven == False:
        stringInput = input(message)
        if stringInput.isdigit() == False:
            print(errormessage)
        else:
            ValidInputGiven = True
    integer = int(stringInput)
    return integer

# list of adjectives
adjectives = ["Attractive","Bald","Beautiful","Chubby","Clean","Dazzling","Drab", "Useless", "Idiotic", "Ferergt", "Disgusting", "Dead", "Dying",]

# list of animals
animals = ["Cow","Rabbit","Ducks","Shrimp","Pig","Goat","Crab","Deer","Bee","Sheep","Fish","Turkey","Dove","Chicken","Horse"]

# get number of players from the user
NumOfPlayers = GetNumberFromUser("what is the number of players that you would like: ", "NOT A NUMBER BAKA")
if NumOfPlayers > 10:
    print("too big bucko, i'm changing it lol")
    NumOfPlayers = 10
elif NumOfPlayers < 3:
    print("too smoll mi amigo, i'm changing it lol")
    NumOfPlayers = 3

# generate names for the number of players
Players = []
for i in range(1, NumOfPlayers + 1):
    player = Player()
    # TODO: make a thing to prevent duplicate names
    player.name = random.choice(adjectives) + random.choice(animals)
    Players.append(player)

print("")
print("PLAYERS")
print("")
for player in Players:
    player.PrintName()

# make up scores, with usernames in order
for player in Players:
    player.score =  random.randrange(0, 10000)

print("")
print("LEADERBOARD")
print("")
Players.sort(key= lambda player: player.score, reverse=True)
for player in Players[:3]:
    player.PrintNameAndScore()