import random

t = ["Rock", "Paper", "Scissors"]


def play_game():
    ai = t[random.randint(0, 2)]
    decision = input("Rock, Paper, Scissors? \n")

    if decision == ai:
        print("Tie")
    elif decision == "Rock":
        if ai == "Paper":
            print("You lose! AI chose " + ai)
        else:
            print("You win! AI sucks, they chose " + ai)
    elif decision == "Paper":
        if ai == "Scissors":
            print("You lose! AI chose " + ai)
        else:
            print("You win! AI sucks, they chose " + ai)
    elif decision == "Scissors":
        if ai == "Rock":
            print("You lose! AI chose " + ai)
        else:
            print("You win! AI sucks, they chose " + ai)


def play_again():
    play = input("Do you want to play again? (yes/no): ")
    return play.lower() == "yes"


print("Let's play best out of 3 against the computer!")
response = input("Do you want to play 3 rounds? (yes/no): ")

if response.lower() == "yes":
    for i in range(3):
        play_game()

while play_again():
    if response.lower() == "yes":
        for i in range(3):
            play_game()

print("Thanks for playing!")
