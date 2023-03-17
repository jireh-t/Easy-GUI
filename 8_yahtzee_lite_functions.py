import easygui, random


def get_name():
    name = easygui.enterbox("Enter name of player")
    return name


def dice():
    # List of numbers in my dice
    nums = ["1", "2", "3", "4", "5", "6"]
    roll = []

    # Shuffles and rolls dice 5 times to get 5 numbers
    for num in range(0, 5):
        random.shuffle(nums)
        roll.append(nums[0])

    roll.sort()  # Sort the numbers from lowest to highest
    return roll


def calc_score(roll):
    counter = 0  # Keep track of the maximum repeats
    for option in roll:  # Loops through every number
        repeats = roll.count(option)  # Counts how many repeats
        if repeats > counter:
            counter = repeats  # Replaces the max if higher

    # Give message and result depending on how many repeats
    if counter == 5:
        return "Yahtzee!", 50
    elif counter == 4:
        return "Four of a kind!", 30
    elif counter == 3:
        return "Three of a kind!", 10
    else:
        return "Better luck next time!", 0


def turn():
    name = get_name()
    turns = 0
    while turns != 3:

        roll = dice()

        # Give the user 2 choices
        choice = easygui.buttonbox(f"{name} dice roll {turns} You "
                                   f"rolled"
                                   f" {', '.join(roll)}\n\n"
                                   f"Choose:", choices=["Roll again", "Stick"])
        turns += 1  # Count the number of turns they've had

        if choice == "Stick":
            easygui.msgbox(f"{roll}\n\n{calc_score(roll[0])}\nScore: "
                           f"{calc_score(roll[1])}")
            turns = 0  # Reset the amount of turns after they choose stick

        # Asks the user to play again if they've had 3 turns
        if turns == 3:
            easygui.msgbox("You ran out of turns. Better luck next time!")


# Main
turn()
