import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_input = input("Rock, Paper, or Scissors? ").lower()
all_plays = [Rock, Paper, Scissors]
comp_play = random.randint(0, 2)

if user_input == "rock":
    print(f"{Rock}\n Computer chose:\n {all_plays[comp_play]}")
elif user_input == "paper":
    print(f"{Paper}\n Computer chose:\n {all_plays[comp_play]}")
elif user_input == "scissors":
    print(f"{Scissors}\n Computer chose:\n {all_plays[comp_play]}")
else:
    print("Hand doesn't exist!")

if user_input == "rock" and comp_play == 0:
    print("Draw")
elif user_input == "rock" and comp_play == 1:
    print("You lost!")
elif user_input == "rock" and comp_play == 2:
    print("You won!")

if user_input == "paper" and comp_play == 0:
    print("You Won!")
elif user_input == "paper" and comp_play == 1:
    print("Draw!")
elif user_input == "paper" and comp_play == 2:
    print("You lost!")

if user_input == "scissors" and comp_play == 0:
    print("You lost!")
elif user_input == "scissors" and comp_play == 1:
    print("You won!")
elif user_input == "scissors" and comp_play == 2:
    print("Draw!")
