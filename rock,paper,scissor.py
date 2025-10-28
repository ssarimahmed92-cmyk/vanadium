import random

player = str(input("Enter rock, paper or scissor: "))

choices = ["rock", "paper", "scissor"]
computer = random.choice(choices)

if player not in choices:
    print("invalid choice")
elif player == computer:
    print("tie")
elif (player == "rock" and computer == "scissor")\
    or (player == "scissor" and computer == "paper")\
    or (player == "paper" and computer == "rock"):
    print(f"computer was {computer}")
    print("you win")
else:
    print(f"computer was {computer}")