import easygui
import random

numbers = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
           "Ten", "Jack", "Queen", "King", "Ace"]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

deck = []
for suit in suits:
    for num in numbers:
        deck.append([num, suit])

while True:

    again = easygui.buttonbox("Do you want to play?", "Welcome", choices=[
        "Yes", "No"])

    if again == "No":
        easygui.msgbox("Goodbye!", "Exit")
        break

    random.shuffle(deck)

    draw = []
    for card in deck[0:7]:
        draw.append(f"Card {deck.index(card)+1}: {card[0]} of {card[1]}")

    for item in draw:
        show_numbers = f"\n*   ".join(draw)

    easygui.msgbox(f"You have drawn\n\n*   {show_numbers}\n\n", "Cards drawn")

