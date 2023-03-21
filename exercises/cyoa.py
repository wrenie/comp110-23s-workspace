"""Choose your own adventure! Hojo Suite 504 edition."""

__author__ = "730566370"

JULIANNA: str = "\U0001F994"  # hedgehog
JORDAN: str = "\U0001F9AD"  # seal
MAGGIE: str = "\U0001F43A"  # wolf
ANNA: str = "\U0001FAB2"  # beetle
CLAIRE: str = "\U0001F429"  # poodle
GRACE: str = "\U0001F98D"  # gorilla
ELIKYA: str = "\U0001F42E"  # cow
WRENE: str = "\U0001F425"  # bird

name_inventory: list[str] = ["Anna", "Maggie", "Claire", "Grace", "Julianna", "Jordan", "Elikya", "Wrene"]
pet_inventory: dict[str, str] = {"ANNA": ANNA, "MAGGIE": MAGGIE, "CLAIRE": CLAIRE, "GRACE": GRACE, "JULIANNA": JULIANNA, "JORDAN": JORDAN, "ELIKYA": ELIKYA, "WRENE": WRENE}
points: int
player: str
pick: str
game_interest: str
choice_interest: str
prize: int


def main() -> None:
    """The starting point of the Suitie game."""
    global points
    global player
    global game_interest
    points = 0
    greet()
    greet_continued()
    interest: str = "YES"
    while interest == "YES":
        print(f"Your current point count is {points} points")
        choices_procedure()
        if game_interest == "NO":
            print(f"Thank you for playing! Your final point count is: {points} points")
            return None
        points += point_choices(points)
        interest = input(f"{player}, do you want to continue and loop back into the Suitie Experience? ")
    if interest == "NO":
        print(f"Your final point count is {points} points")
        print("Thank you for playing!")
    

def greet() -> None:
    """Welcome message and greeting for the game."""
    global pick
    global player
    player = input("Hello! Please enter your name: ")
    print(f"Welcome, {player} to the game. This is Taking Care of Suite 504!")
    print("The goal of this game is to keep Suite 504 happy and healthy! The higher your point count, the better pet owner you are!")
    print("You will select a suitie to take care of, and each suitie has a corresponding emoji that represents them.")
    print()
    print("When responding to prompts, please respond in CAPITAL letters with no extra spaces or characters.")
    print()
    print("Here are your suitie options!")
    print("Anna, Maggie, Claire, Grace, Julianna, Jordan, Elikya, and Wrene")


def greet_continued() -> None:
    """Continuation of introduction to the game."""
    global player
    global pick
    idx = 0
    for elem in pet_inventory:
        emoji_assign = pet_inventory[elem]
        name_assign = name_inventory[idx]
        print(f"{name_assign} is {emoji_assign}!")
        idx += 1
    print()
    pick = input("Remembering to respond in CAPITALS, please select a suitie: ")
    if pick == 'WRENE' or pick == "ANNA" or pick == "ELIKYA" or pick == "JORDAN" or pick == "JULIANNA" or pick == "GRACE" or pick == "CLAIRE" or pick == "MAGGIE":
        sure: str = input(f"Are you sure you want to pick {pick}? Please respond with YES or NO: ")
    else:
        pick = input("That's not a suitie! Please respond in CAPITALS with a suitie name: ")
    while sure == "NO":
        pick = input("Please choose another suitie: ")
        while pick != 'WRENE' and pick != "ANNA" and pick != "ELIKYA" and pick != "JORDAN" and pick != "JULIANNA" and pick != "GRACE" and pick != "CLAIRE" and pick != "MAGGIE":
            pick = input("That's not a suitie! Please respond in CAPITALS with a suitie name: ")
        sure = input(f"Are you sure you want to pick {pick}? Please select YES or NO: ")
    print()
    if sure == "YES":
        print(f"Yay! {pick} is so excited to come home with you!")
        print(pet_inventory[pick] + " is a very cute pet to choose!")
        print()
    else:
        while sure != "YES" and sure != "NO":
            sure = input("Please select either YES or NO: ")
    print(f"During this game, you will take care of {pick} and make choices that will add or subtract points from your point count!")


def point_counter(answer: str) -> int:
    """A function that tallies points based on "bad", "good", or "neutral" decisions."""
    global points
    if answer == "D":
        print("You chose to end the game here!")
        print(f"Your total point count is: {points}")
        return points
    while answer != "A" and answer != "B" and answer != "C":
        answer = input("Please respond with A, B, or C: ")
    if answer == "A":
        points += 1
    if answer == "B":
        points += 0
    if answer == "C":
        points += -1
    return points


def response() -> str:
    """Takes the input from user and turns it into an answer."""
    answer: str = input("Please select A, B, or C to continue, and D to end the game: ")
    print()
    return answer


def choices_procedure() -> None:
    """The procedure where choices are made by the player."""
    global game_interest
    global choice_interest
    global player
    global points
    global pick
    game_interest = input(f"{player}, do you still want to play the Suitie game? YES or NO: ")
    if game_interest == "NO":
        print("Thank you for playing the suitie game!")
        print(f"Your total point count is: {points}")
    else:
        choice_interest = "YES"
    while choice_interest == "YES":
        print()
        print(f"{pick} is sick! What will you do?")  # choice 1
        print("A: Bring them crackers and water") 
        print("B: Nothing")
        print("C: Shove them down the Hojo stairs since you're annoyed")
        print("D: End my Suitie experience")
        answer1: str = response()
        print()
        point_counter(answer1)
        if answer1 == "A":
            print(f"Yay! {pick} feels all better now!")
        if answer1 == "B":
            print(f"Aww :( {pick} understands why you didn't want to help them, but is sad anyways")
        if answer1 == "C":
            print(f"{pick} broke their leg after falling down the stairs.")
            print(f"{pick} refuses to talk to you now. What will you do?")
            print("A: Apologize and help them heal their leg")
            print("B: Bring them a bandaid")
            print("C: Spit in their face")
            print("D: End my Suitie experience")
            answer1C: str = response()
            point_counter(answer1C)
            if answer1C == "NO":
                game_interest == "NO"
                choice_interest == "NO"
        if answer1 == "D":
            game_interest = "NO"
            choice_interest = "NO"
            return None
        print(f"{pick} wants to go somewhere with you! Where will you go?")  # choice 2
        print("A: Go to the movies")
        print("B: Don't go anywhere")
        print("C: Go to the city junkyard")
        print("D: End my Suitie experience")
        answer1A: str = response()
        print()
        point_counter(answer1A)
        if answer1A == "D":
            game_interest = "NO"
            choice_interest = "NO"
            return None
        print(f"Now, {pick} wants to have dinner with you. Where do you want to go?")  # choice 3
        print("A: Go to Spicy 9")
        print("B: Have dinner at home")
        print(f"C: Tell {pick} you don't want anything to do with them")
        print("D: End my Suitie experience")
        answer1B: str = response()
        print()
        point_counter(answer1B)
        if answer1B == "D":
            game_interest = "NO"
            choice_interest = "NO"
            return None
        if game_interest == "YES":
            choice_interest = input(f"{player}, do you want to restart this choice chain? YES or NO: ")
        if game_interest == "YES" and choice_interest == "NO":
            print("Okay! On to the next Suitie experience!")
            print()
        elif game_interest == "NO":
            print("Okay! The Suitie Experience will end shortly!")
            choice_interest = "NO"
        

def point_choices(points: int) -> int:
    """Takes the player's point value as input and returns the total points after some choices are made."""
    from random import randrange
    global pick
    print(f"Your friend, {pick}, really wants to play the lottery!")  # choice 4
    print("What amount of money do you want to use to buy a ticket?")
    print("A: $20")
    print("B: $5")
    print("C: $1")
    answer3: str = input("Please select A, B, or C: ")
    if answer3 == "A":
        prize = randrange(0, 10000, 50)
    if answer3 == "B":
        prize = randrange(0, 100, 5)
    if answer3 == "C":
        prize = randrange(-10, 20, 1)
    while answer3 != "A" and answer3 != "B" and answer3 != "C":
        answer3 = input("That wasn't A, B or C! Try again: ")
    print("It's time to see what you won!")
    print(f"You won {prize} dollars!")
    print("This value will be added to your point count!")
    print("If you were stingy with your money... RIP your points :(")
    return prize


if __name__ == "__main__":
    main()