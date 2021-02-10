import random
print ("HELLO!!!")

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
elif NumOfPlayers < 2:
    print("too smoll mi amigo, i'm changing it lol")
    NumOfPlayers = 2

# generate names for the number of players 
NaMeS = []
for i in range(1, NumOfPlayers + 1):
    naming = random.choice(adjectives) + random.choice(animals)
    NaMeS.append(naming)

for name in NaMeS:
    print(name)

# make up 3 scores, with usernames in order
# def NameGenerator():