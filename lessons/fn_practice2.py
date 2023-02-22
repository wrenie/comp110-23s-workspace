"""Function writing practice."""

def mimic(my_words: str, letter_idx: int) -> str:
    """outputs the character of my_words at index letter_idx"""
    if letter_idx > len(my_words)-1:
        return "Too high of a number"
    else:
        mimic_letter: str = my_words[letter_idx]
        return mimic_letter

mimic("heyshawty",3)
print(mimic("heyshawty",3))

mimic("heyshawty",13)
print(mimic("heyshawty",13))
