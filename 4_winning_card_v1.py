import easygui
import random

numbers = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
           "Ten", "Jack", "Queen", "King", "Ace"]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

play = easygui.buttonbox("Would you like to play?", "Welcome", choices=[
    "Yes", "No"])

while play == "Yes":
    comp_num = random.choice(numbers)
    comp_suit = random.choice(suits)

    player_num = random.choice(numbers)
    player_suit = random.choice(suits)

    easygui.msgbox(f"Computer got the {comp_num} of {comp_suit}\n"
                   f"Player got the {player_num} of {player_suit}","Cards")

    if numbers.index(comp_num) > numbers.index(player_num):
        easygui.msgbox("Computer has the winning card", "Result")

    elif numbers.index(comp_num) < numbers.index(player_num):
        easygui.msgbox("Player has the winning card", "Result")

    elif numbers.index(comp_num) == numbers.index(player_num):
        easygui.msgbox("It was a tie", "Result")

    play = easygui.buttonbox("Would you like to play?", "Welcome", choices=[
    "Yes", "No"])

easygui.msgbox("Goodbye")
