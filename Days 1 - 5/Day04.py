# Day 4 - Randomisation and Python Lists
"""
Not implementing a scoring system.
"""
import random

rock_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_ascii = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice_list = ["rock", "paper", "scissors"]

while True:
    choose = input("Make your choice here: ").lower()
    choice = random.choice(choice_list)
    if choose not in choice_list:
        print("Stop waisting my time!")
    if choose == choice:
        print(f"You both choose {choose}")
        print("Draw!")
    elif choose == "rock":
        print(f"You chose {choose}")
        print(f"The computer Chose {choice}")
        if choice == "scissors":
            print("You win!")
        else:
            print("You Loose!")
    elif choose == "paper":
        print(f"You chose {choose}")
        print(f"The computer Chose {choice}")
        if choice == "rock":
            print("You win!")
        else:
            print("You win!")
    elif choose == "scissors":
        print(f"You chose {choose}")
        print(f"The computer Chose {choice}")
        if choice == "paper":
            print("You Win!")
        else:
            print("You Loose!")
