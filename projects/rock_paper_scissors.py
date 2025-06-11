"""
Write a Python program that allows the user to play a game of Rock, Paper, Scissors against the computer.
The program should:

1. Continuously prompt the user to enter "Rock", "Paper", or "Scissors" (case-insensitive), or "Q" to quit.

2. Randomly generate the computer's choice.

3. Compare the user's input to the computer's choice to determine the winner:

- Rock beats Scissors

- Scissors beats Paper

- Paper beats Rock

4. Keep track of how many times the user and the computer win.

5. Display the result of each round and, when the user quits, print the final scores before exiting.
"""

import random
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
options[0]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
        
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")