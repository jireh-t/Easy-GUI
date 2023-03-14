import easygui
import random

while True:
    weapons = ["Paper", "Scissors", "Rock"]
    computer = random.choice(weapons)
    play_again = easygui.buttonbox("Welcome to Paper, Scissors, Rock\n\n"
                                   "Rock beats scissors\n"
                                   "Scissors beats paper\n"
                                   "Paper beats rock\n"
                                   "Do you want to play?\n",
                                   "Welcome and Rules", choices=["Yes",
                                                                   "No"])
    if play_again == "No":
        break
    else:
        choice = easygui.buttonbox("Choose your weapon", "Choose weapon",
                                   choices = [weapons[0], weapons[1],
                                              weapons[2]])
        easygui.msgbox(f"You chose {choice} and the computer chose "
                       f"{computer}", "Choice")

        if computer == choice:
            results = "This was a draw"
        elif computer == "Paper" and choice == "Rock" or computer == "Rock" \
                and choice == "Scissors" or computer == "Scissors" and \
                choice == "Paper":
            results = "You lose"
        else:
            results = "You win"

        easygui.msgbox(f"{results}", "Results")
print("Goodbye")
