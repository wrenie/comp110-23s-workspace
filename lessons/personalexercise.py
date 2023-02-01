"""A guessing game for a number"""

__author__ = "730566370"

import random
x = random.randint(1,100)

guess = input("Guess a number between 0 and 100! ")

if int(guess) > x:
    print("Too big! choose a smaller number")

if int(guess) < x:
    print("Too small! choose a bigger number")

if int(guess) == x:
    print("You guessed correctly!")
    exit()

print(x)
