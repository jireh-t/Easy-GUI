"""Modification to yahtzee v1, allowing for two players and scoring system
using functions"""

# Importing my modules
import easygui
import random


# Function to ask the players name
def get_name(number):
    name = easygui.enterbox(f"Enter name of player {number}")
    return name


# Function to roll the dice and output the user's roll
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


# Calculate the user's score after they have sticked or run out of turns
def calc_score(roll):
    counter = 0  # Keep track of the maximum repeats
    for option in roll:  # Loops through every number
        repeats = roll.count(option)  # Counts how many repeats
        if repeats > counter:
            counter = repeats  # Replaces the max if higher

    # Give message and result depending on how many repeats
    if counter == 5:
        return ["Yahtzee!", 50]
    elif counter == 4:
        return ["Four of a kind!", 30]
    elif counter == 3:
        return ["Three of a kind!", 10]
    else:
        return ["Better luck next time!", 0]


# Function to run the player's turn
def turn(name):
    turns = 0  # Keep track of what turn they're on
    while turns != 3:
        roll = dice()

        # Give the user 2 choices
        choice = easygui.buttonbox(f"{name} dice roll {turns + 1}\n "
                                   f"You rolled"
                                   f" {', '.join(roll)}\n\n"
                                   f"Choose:", choices=["Roll again", "Stick"])
        turns += 1  # Count the number of turns they've had

        if choice == "Stick":
            return roll

        # Asks the user to play again if they've had 3 turns
        if turns == 3:
            easygui.msgbox("You ran out of turns")
            return roll


# Function to output the winner and result
def result(p1_score, p2_score, p1_name, p2_name):
    if p1_score[1] > p2_score[1]:
        easygui.msgbox(f"The winner is {p1_name} with a score of "
                       f"{p1_score[1]}\n\n"
                       f"{p2_name} scored {p2_score[1]}")
    elif p2_score[1] > p1_score[1]:
        easygui.msgbox(f"The winner is {p2_name} with a score of "
                       f"{p2_score[1]}\n\n"
                       f"{p1_name} scored {p1_score[1]}")
    elif p1_score[1] == p2_score[1]:
        easygui.msgbox(f"It was a draw!\n\n"
                       f"{p1_name} scored {p1_score[1]} and {p2_name} also "
                       f"scored {p2_score[1]}")


# Main

# Get the player's names
p1 = get_name(1).title()
p2 = get_name(2).title()

# Welcome the players and give the option to play or not
again = easygui.buttonbox(f"Welcome {p1} and {p2} would you like to play?",
                          "Welcome", choices=["Yes", "No"])


# Keep looping the game until the user wants to quit
while True:
    if again == "No":
        easygui.msgbox("Goodbye!", "Exit")
        break

    # Run player 1's turn
    easygui.msgbox(f"Get ready to roll {p1}!")
    roll1 = turn(p1)
    score1 = calc_score(roll1)

    # Print player 1's score
    easygui.msgbox(f"{', '.join(roll1)}\n\n"
                   f"{score1[0]}\n"
                   f"Score: {score1[1]}")

    # Run player 2's turn
    easygui.msgbox(f"Get ready to roll {p2}!")
    roll2 = turn(p2)
    score2 = calc_score(roll2)

    # Print player 2's score
    easygui.msgbox(f"{', '.join(roll2)}\n\n"
                   f"{score2[0]}\n"
                   f"Score: {score2[1]}")

    # Print the result
    result(score1, score2, p1, p2)

    # Ask if they want to play again
    again = easygui.buttonbox("Would you like to play again?", "Again?",
                              choices=["Yes", "No"])
