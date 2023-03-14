""" A program that gets a NZ English word and converts it to US spelling"""

import easygui

# Asks the user to play
again = easygui.buttonbox("Would you like to enter a word?",
                          "Welcome", choices=["Yes", "No"])

# loop for the user to continue playing again
while again == "Yes":

    nz_word = easygui.enterbox("Enter NZ English word", "NZ")
    letters = list(nz_word)  # Converts word to list so we can remove later

    # Check if user has entered a word that should be changed or replaced

    if "our" in nz_word:
        letters.remove("u")
        us_word = "".join(letters)
        easygui.msgbox(f"The US spelling for {nz_word} is {us_word}", "US")

    elif "ise" in nz_word:
        us_word = nz_word.replace("ise", "ize")
        easygui.msgbox(f"The US spelling for {nz_word} is {us_word}", "US")

    elif "yse" in nz_word:
        us_word = nz_word.replace("yse", "yze")
        easygui.msgbox(f"The US spelling for {nz_word} is {us_word}", "US")

    else:  # If the user has entered a word that doesn't need to be changed
        easygui.msgbox("The spelling is the same for NZ and US", "No change")

    # Ask user to play again
    again = easygui.buttonbox("Would you like to enter another word?",
                              "Again?", choices=["Yes", "No"])

easygui.msgbox("Goodbye")
