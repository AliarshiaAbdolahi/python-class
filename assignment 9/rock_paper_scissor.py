import random
import pyfiglet

title = pyfiglet.figlet_format("ROCK---PAPER                   SCISSORS")
print(title)

loop = int(input("How many time do you want to play: "))
loop += 1
win = 0
lost = 0
tied = 0

for i in range(1,loop):
    print('Rock - Paper - scissors')

    Player = input('Please enter your choise: ')

    number = random.randint(1,3)
    user = ""
    if number == 1:
        user = "rock"
        print("User choise=> (Rock)")

    elif number == 2:
        user = "paper"
        print("User choise=> (Paper)")

    elif number == 3:
        user = "scissors"
        print("User choise=> (Scissors)")
        
    if user == 'rock' and Player == 'rock':
        print("The game was tied !")
        tied += 1

    elif user == 'rock' and Player == 'paper':
        print("You won the game ✔")
        win += 1

    elif user == 'rock' and Player == 'scissors':
        print("You lost the game ❌")
        lost += 1
        
    elif user == 'scissors' and Player == 'rock':
        print("You won the game ✔")
        win += 1

    elif user == 'paper' and Player == 'rock':
        print("You won the game ✔")
        win += 1

    elif user == 'paper' and Player == 'paper':
        print("The game was tied !")

    elif user == 'paper' and Player == 'scissors':
        print("You won the game ✔")
        tied += 1

    elif user == 'scissors' and Player == 'paper':
        print("You lost the game ❌")
        lost += 1

    elif user == 'scissors' and Player == 'scissors':
        print("The game was tied !")
        tied += 1
print("win:",win)
print("lost:",lost)
print("tied:",tied)
