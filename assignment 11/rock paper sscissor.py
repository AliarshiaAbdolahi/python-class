import random

def check_win(user,computer):
    if (user == "r" and computer == "s" ) or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
        return True
def rock_paper_sccisor():
    player = input("What is your choies - 'r' for rock, 's' for sccisor, 'p' for paper: ")
    choices = ['r','s','p']
    opponent = random.choice(choices)

    if player == opponent:
        return print(f"Ist a Tie! computer choice is {opponent}")
    if check_win(player,opponent):
        return print(f"Yay! You won! computer choiec is {opponent}")
    if check_win(player,opponent) != True:
        return print(f"You lost! computer choice is {opponent}")
    
rock_paper_sccisor()