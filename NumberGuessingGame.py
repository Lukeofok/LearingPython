# Create a number guessing game where the user has to guess a randomly generated number.
# Concepts: Loops, conditionals, random module.

import random

# check if the guess vs the answer
def check_guess(answer, guess):

    if guess > answer:
        print(f"\nYour guess is GRATER than the nubmer I am thinking of.")
        return(1)
    elif guess < answer:
        print(f"\nYour guess is LESS than the nubmer I am thinking of.")
        return(-1)
    else:
        print(f"\nYou win!!! my number was {answer}\n")
        return(0)

# prints the new range for guessing
def update_range(check, guess):

    return()

# generate random number
answer = random.randint(1,1000)
answer_range = [1,1000]

# intro
print("I am thinking of a nubmer between 1-1000.")
guess = int(input(f"What number am I thinking of? "))
number_of_guesses = 1

# main
while True:
    check = check_guess(answer, guess)

    if check == 0:
        break
    else:
        answer_range = update_range(check, guess)

    number_of_guesses += 1
    print(f"Guess {number_of_guesses}")
    print(f"Here is the range of numbers it could be. ***")
    guess = int(input(f"\nWhat is your new guess? "))