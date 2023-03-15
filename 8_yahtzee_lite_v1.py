"""Simplified version of Yahtzee! Lite game"""

# Importing my modules
import easygui
import random

# List of numbers in my dice
dice = ["1", "2", "3", "4", "5", "6"]

# Welcome the user and give the option to play or not
again = easygui.buttonbox("Welcome, would you like to play?", "Welcome",
                          choices=["Yes", "No"])

# Loops the game as long as the user wants to keep playing
while True:
    turns = 0

    # End the game if the user wants to exit
    if again == "No":
        easygui.msgbox("Goodbye!", "Exit")
        break

    while turns != 3:
        roll = []

        # Shuffles and rolls dice 5 times to get 5 numbers
        for num in range(0, 5):
            random.shuffle(dice)
            roll.append(dice[0])

        roll.sort()  # Sort the numbers from lowest to highest

        # Give the user 2 choices
        choice = easygui.buttonbox(f"You rolled {', '.join(roll)}\n\n"
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
                easygui.msgbox(f"{', '.join(roll)}\n\n Yahtzee!")
            elif counter == 4:
                easygui.msgbox(f"{', '.join(roll)}\n\n Four of a kind!")
            elif counter == 3:
                easygui.msgbox(f"{', '.join(roll)}\n\n Three of a kind!")
            else:
                easygui.msgbox("Better luck next time!")

            again = easygui.buttonbox("Do you want to play another round?",
                                      "Goodbye", choices=["Yes", "No"])
            turns = 0  # Reset the amount of turns after they choose stick
            if again == "No":
                break

        # Asks the user to play again if they've had 3 turns
        if turns == 3:
            again = easygui.buttonbox("You've had 3 turns. Do you want to play "
                                      "another round?", "Goodbye",
                                      choices=["Yes", "No"])
