import random

def dice1():
    print("---------")
    print("|       |")
    print("|   0   |")
    print("|       |")
    print("---------")

def dice2():
    print("---------")
    print("|  0    |")
    print("|       |")
    print("|    0  |")
    print("---------")

def dice3():
    print("---------")
    print("|  0    |")
    print("|   0   |")
    print("|    0  |")
    print("---------")

def dice4():
    print("---------")
    print("| 0   0 |")
    print("|       |")
    print("| 0   0 |")
    print("---------")

def dice5():
    print("---------")
    print("| 0   0 |")
    print("|   0   |")
    print("| 0   0 |")
    print("---------")

def dice6():
    print("---------")
    print("| 0   0 |")
    print("| 0   0 |")
    print("| 0   0 |")
    print("---------")


print("Hello User")

n = input("Type 'y' to roll the dice or 'n' to quit: ")

if(n == 'y'):

    x = random. randint(1,7)

    if(x == 1):
        dice1()
    elif x == 2:
        dice2()
    elif x == 3:
        dice3()
    elif x == 4:
        dice4()
    elif x == 5:
        dice5()
    else:
        dice6()

if n == 'n':
    print("Thanks for your time :)")