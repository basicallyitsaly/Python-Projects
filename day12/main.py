import art
import random

# Create the random number
number_to_guess = random.randint(1, 100)

#Intro
print(art.logo)
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")


def solving_game():
    guesses_left = 0
    if difficulty == "easy":
        guesses_left = 10
    if difficulty == "hard":
        guesses_left = 5


    while guesses_left > 0:
        print(f"You have {guesses_left} attempts remaining to guess the number.")
        print(f"Number to guess is {number_to_guess}.")
        guess = int(input("Make a guess: "))
        if guess == number_to_guess:
            guesses_left = 0
            print(f"You win! the number was {number_to_guess}.")
        if guess > number_to_guess:
            print("Too high!")
            guesses_left -= 1
        elif guess > 100 or guess < 0:
            print("That number is out of bounds! Please try again.")
        if guess < number_to_guess:
            print("Too low!")
            guesses_left -= 1


    if guesses_left == 0:
        print("You ran out of guesses! You lose!")


solving_game()
