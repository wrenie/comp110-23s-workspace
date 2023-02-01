"""One shot wordle!"""
__author__ = "730566370"

secret = "python"
secret_length = len(secret)

guess = input(F"What is your {secret_length}-letter guess? ")
while len(guess) != len(secret):
    guess = input(F"That was not {secret_length} letters! Try again: ")

white: str = "\U00002B1C"
green: str = "\U0001F7E9"
yellow: str = "\U0001F7E8"

word_index: int = 0
emoji: str = ""

while word_index < secret_length:
    if guess[word_index] == secret[word_index]:
        emoji = emoji + green
    else:
        index2: int = 0
        in_word: bool = False
        while in_word is not True and index2 < secret_length:
            if guess[word_index] == secret[index2]:
                in_word = True
            index2 = index2 + 1
        if in_word is True:
            emoji = emoji + yellow
        else:
            emoji = emoji + white
    word_index = word_index + 1
print(emoji)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")