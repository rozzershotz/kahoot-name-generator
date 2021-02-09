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

adjectives = ["attractive","bald","beautiful","chubby","clean","dazzling","drab", "useless", "idiotic", "ferergt", "disgusting", "dead", "dying",]


animals = ["Cow","Rabbit","Ducks","Shrimp","Pig","Goat","Crab","Deer","Bee","Sheep","Fish","Turkey","Dove","Chicken","Horse"]

GetNumberFromUser("what is the number of players that you would like: ", "NOT A NUMBER BAKA")

def NameGenerator():
    Number = integer
    if Number >= 10:
        print("too big bucko")
        GridSize = 20
    elif GridSize <= 2:
        print("too smoll mis amigo")
