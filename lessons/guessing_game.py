"""A guessing game for a number"""

__author__ = "730566370"

SECRET: int = 4
guess: int = int(input("Guess a number between 0 and 10! "))
playing: bool = True
idx: int = 1

while playing and idx < 3:
    print("Number of guesses: " + str(idx))
    if idx == 3:
        print("Last guess!")
    if int(guess) == SECRET:
        print("You guessed correctly!")
        playing = False
    else:
        if guess % 2 == 1: #guess is odd
            print("Your guess is odd. The answer is even!")
        if int(guess) < SECRET:
            print("Too small! choose a bigger number")
        if int(guess) > SECRET:
            print("Too big! choose a smaller number")
        guess = int(input("Make another guess! "))
    idx = idx + 1
    print(" ")

if guess == SECRET:
    print(F"Yay! {SECRET} was the correct guess!")
