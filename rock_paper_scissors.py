import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to rock, paper, scissors. In this game you and your opponent choose one of these three things.")
print("Rock blunts scissors. Paper covers rock. Scissors cut paper.")

valid_choices = ["rock", "r", "paper", "p", "scissors", "s"]
# p = player_choice and c = computer_choice
p = None

while p not in valid_choices:
    p = input("Please make your choice: ").casefold()

if p == "rock" or p == "r":
    print("You chose Rock.")
    print(rock)
    p = "rock"
elif p == "paper" or p == "p":
    print("You chose Paper.")
    print(paper)
    p = "paper"
else:
    print("You chose Scissors.")
    print(scissors)
    p = "scissors"

c = random.choice(["rock", "paper", "scissors"])

if c == "rock":
    print("Computer chose Rock.")
    print(rock)
elif c == "paper":
    print("Computer chose Paper.")
    print(paper)
else:
    print("Computer chose Scissors.")
    print(scissors)

if p == c:
    print("This game was a tie!")
elif (p == "rock" and c == "scissors") or (p == "paper" and c == "rock") or (p == "scissors" and c == "paper"):
    print("Well Done! You win!")
else:
    print("Bad luck. The computer won!")
