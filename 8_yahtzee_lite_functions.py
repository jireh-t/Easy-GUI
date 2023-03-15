import easygui, random

def turn():
    roll = []

    # Shuffles and rolls dice 5 times to get 5 numbers
    for num in range(0, 5):
        random.shuffle(dice)
        roll.append(dice[0])

    roll.sort()  # Sort the numbers from lowest to highest

    # Give the user 2 choices
    choice = easygui.buttonbox(f"{player1} dice roll {turns1} You rolled"
                               f" {', '.join(roll)}\n\n"
                               f"Choose:", choices=["Roll again", "Stick"])

    turns += 1  # Count the number of turns they've had

    if choice == "Stick":
        counter = 0  # Keep track of the maximum repeats
        for option in roll:  # Loops through every number
            repeats = roll.count(option)  # Counts how many repeats
            if repeats > counter:
                counter = repeats  # Replaces the max if higher

        # Give message and result depending on how many repeats
        if counter == 5:
            easygui.msgbox(f"{', '.join(roll)}\n\n Yahtzee!\n Score: 50")
            score1 += 50
        elif counter == 4:
            easygui.msgbox(f"{', '.join(roll)}\n\n Four of a kind!\n "
                           f"Score: 30")
            score1 += 30
        elif counter == 3:
            easygui.msgbox(f"{', '.join(roll)}\n\n Three of a kind!\n "
                           f"Score: 10")
        else:
            easygui.msgbox("Better luck next time!")

        again = easygui.buttonbox("Do you want to play another round?",
                                  "Goodbye", choices=["Yes", "No"])

        turns = 0  # Reset the amount of turns after they choose stick
        if again == "No":
            break
