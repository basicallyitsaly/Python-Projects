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

move = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
#My move
if move == 0:
    print(rock)
elif move == 1:
    print(paper)
elif move == 2:
    print(scissors)
else:
    print("Invalid input")

#opponent move
print("Conputer chose:")
opponent = random.choice(["Rock", "Paper", "Scissors"])
if opponent == "Rock":
    result = "Rock"
    print(rock)
elif opponent == "Paper":
    result = "Paper"
    print(paper)
else:
    result = "Scissors"
    print(scissors)

#Score
if move == 0 and result == "Paper":
    print("You lose")
elif move == 0 and result == "Rock":
    print("It's a draw")
elif move == 0 and result == "Scissors":
    print("You win")
elif move == 1 and result == "Rock":
    print("You win")
elif move == 1 and result == "Scissors":
    print("You lose")
elif move == 1 and result == "Paper":
    print("It's a draw")
elif move == 2 and result == "Rock":
    print("You lose")
elif move == 2 and result == "Paper":
    print("You win")
elif move == 2 and result == "Scissors":
    print("It's a draw")

