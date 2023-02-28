"""A structured wordle."""

__author__ = "730566370"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret_word: str = "codes"
    secret_length: int = len(secret_word)
    while turn < 7:
        print(F"=== Turn {turn}/6 ===")
        guessed: str = input_guess(secret_length)
        print(emojified(guessed, secret_word))
        if guessed == secret_word:
            print(F"You won in {turn}/6 guesses!")  # the user has won!
            return None
        else:  # if they didn't guess the word move to the next turn
            turn = turn + 1
    print("X/6 - Sorry, try again tomorrow")
    return None


def contains_char(search_word: str, search_char: str) -> bool:
    """Looks to see if the given character is inside of a word being searched."""
    assert len(search_char) == 1
    search_idx: int = 0
    while search_idx < len(search_word):
        if search_word[search_idx] == search_char:
            return True  # will return true and exit if the character is found in the word
        search_idx = search_idx + 1
    return False  # returns false if the character is not found in the word


def emojified(guess: str, secret: str) -> str:
    """Tests for green, yellow, and white emoji boxes and returns a string of emojis that corresponds to the given guess/secret."""
    assert len(guess) == len(secret)
    WHITE: str = "\U00002B1C"
    GREEN: str = "\U0001F7E9"
    YELLOW: str = "\U0001F7E8"
    
    word_index: int = 0
    emoji: str = ""

    while word_index < len(secret):
        if guess[word_index] == secret[word_index]:  # if the letter is in the correct position
            emoji = emoji + GREEN
        else:
            in_word: bool = contains_char(secret, guess[word_index])
            if in_word is True:
                emoji = emoji + YELLOW
            else:  # the letter is not in the word at all
                emoji = emoji + WHITE
        word_index = word_index + 1
    return emoji


def input_guess(expect_len: int) -> str:
    """Checks to make sure the length of the input matches the wanted length."""
    guessed = input(f"Enter a {expect_len} character word: ")
    # loops repeatedly until the input is the correct length
    while len(guessed) != expect_len:
        guessed = input(f"That wasn't {expect_len} chars! Try again: ")
    return guessed
    

if __name__ == "__main__":
    main()