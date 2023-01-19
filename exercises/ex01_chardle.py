"""EX01 - Chardle: a miniature version of Wordle!"""

__author__ = "730566370"

attempt_word: str = input("Enter a 5-character word: ")
if len(attempt_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

attempt_chr: str = input("Enter a single character: ")
if len(attempt_chr) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + attempt_chr + " in " + attempt_word)

count = int(0)

if (attempt_chr == attempt_word[0]):
    print(attempt_chr + " found at index 0")
    count = count + 1


if (attempt_chr == attempt_word[1]):
    print(attempt_chr + " found at index 1")
    count = count + 1

if (attempt_chr == attempt_word[2]):
    print(attempt_chr + " found at index 2")
    count = count + 1

if (attempt_chr == attempt_word[3]):
    print(attempt_chr + " found at index 3")
    count = count + 1

if (attempt_chr == attempt_word[4]):
    print(attempt_chr + " found at index 4")
    count = count + 1

if count == 0:
    print("No instances of " + attempt_chr + " found in " + attempt_word)

if count == 1:
    print(str(count) + " instance of " + attempt_chr + " found in " + attempt_word)

if count >= 2:
    print(str(count) + " instances of " + attempt_chr + " found in " + attempt_word)