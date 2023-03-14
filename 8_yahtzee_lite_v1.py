"""Simplified version of Yahtzee! Lite game"""

# Importing my modules
import easygui
import random

dice = [1, 2, 3, 4, 5, 6]

while True:
    turns = 0
    again = easygui.buttonbox("Welcome, would you like to play?", "Welcome",
                              choices=["Yes", "No"])
    if again == "No":
        easygui.msgbox("Goodbye!", "Exit")
        break

    while True:
        roll = []

        for num in range(0, 5):
            random.shuffle(dice)
            roll.append(dice[0])

        roll.sort()

        choice = easygui.buttonbox(f"You rolled {roll}\n\n"
                                   f"Choose:", choices=["Roll again", "Stick"])
        turns += 1

        if choice == "Stick":
            counter = 0
            for option in roll:
                repeats = roll.count(option)
                if repeats > counter:
                    repeats = counter

            if counter == 5:
                easygui.msgbox(f"{roll}\n\n Yahtzee!")
            elif counter == 4:
                easygui.msgbox(f"{roll}\n\n Four of a kind!")
            elif counter == 3:
                easygui.msgbox(f"{roll}\n\n Three of a kind!")
            else:
                easygui.msgbox("Better luck next time!")


        if turns == 3:
            again = easygui.buttonbox("You've had 3 turns. Do you want to play "
                                      "another round?", "Goodbye",
                                      choices=["Yes", "No"])





