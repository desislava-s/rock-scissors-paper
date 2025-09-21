import sys
import random

rock = 'rock'
scissors = 'scissors'
paper = 'paper'

player_move = input("Choose [r]ock, [s]cissors, [p]aper: ").lower()

if player_move == "r":
    player_move = rock
elif player_move == "s":
    player_move = scissors
elif player_move == "p":
    player_move = paper
else:
    print("Invalid input!Exiting the game...")
    sys.exit()

options = ["rock", "scissors", "paper"]
computer_move = random.choice(options)
print(f"The computer chose {computer_move}.")

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")
