# program for rock, paper and scissor game
import random

print("welcome to rock, paper and scissor game")

options = ["rock", "paper", "scissor"]

user_choice = int(input("what do you choose? Type 0 for rock, 1 for paper and 2 for scissor"))
computer_choice = random.randint(0, 2)

print(f"You chose: {options[user_choice]}")
print(f"Computer chose: {options[computer_choice]}")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice == user_choice:
    print("It's a draw!")
elif user_choice > computer_choice:
    print("You win!")
else:
    print("You typed an invalid number. You lose!")