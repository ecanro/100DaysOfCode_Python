#Number Guessing Game Objectives:

# Include an ASCII art logo.
from arts_pro import logo12
print(logo12)

import random
print("Welcome to the Number Guessing Game!")
# Allow the player to submit a guess for a number between 1 and 100.
number = random.randrange(1, 100)
print("I'm thinking of a number between 1 to 100.")
difficulty = input("Choose a difficulty, Type 'easy' or 'hard': ")
attempts = 0
if difficulty == 'easy':
    attempts = 10
    print(f"You have {attempts} attempts remaining to gues the number.")
else:
    attempts = 5
    print(f"You have {attempts} attempts remaining to gues the number.")
while attempts:
    attempts -= 1
    guess = int(input("Make a guess: "))
    if attempts == 0:
        print("You've run out of guesses, you lose")
    elif number == guess:
        attempts = 0
        print(f"You got it, the answer was {number}")
    elif number > guess:
        print('Too low')
        print('Guess again.')
        print(f"You have {attempts} attempts remaining to gues the number.")
    elif number < guess:
        print('Too high')
        print('Guess again.')
        print(f"You have {attempts} attempts remaining to gues the number.")

    