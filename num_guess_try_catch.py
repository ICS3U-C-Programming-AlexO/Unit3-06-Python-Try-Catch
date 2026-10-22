#!/usr/bin/env python3
# Created by: Alex OBrien
# Created on: October 20, 2026
# This program uses a try catch program to create a 
# random number guesser game

import random

def main():
    # Generate a random int between 0 and 9
    random_num = random.randint(0, 9)

    user_input = input("   Guess a random number between 0-9! : ")
    try:
        # Attempt to convert user input to int
        guess_num = int(user_input)
    except ValueError:
        # If user input cannot be converted into int
        print(f"'{user_input}' isn't a valid input!")
        return

    # Check the guess
    if random_num != guess_num:
        print("You guessed incorrectly!")
        print(f"The correct number was {random_num}")
    else:
        print("You guessed correctly!")

if __name__ == "__main__":
    main()