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


print("\nHello User\n")

n = input("Type 'y' to roll the dice or 'n' to quit: ")

while(n != 'y' and n != 'n'):
    print("Please enter the right letter\n")
    n = input("Type 'y' to roll the dice or 'n' to quit: ")
    while n == 'y':

        x = random. randint(1,7)
        print("\n")
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
        print("\n")
        n = input("Wanna roll dice again, just type 'y': ")
        print("\n")

    if n == 'n':
        print("\nThanks for your time :)")
        print("Have a good time :)")
        print("\n")
    
