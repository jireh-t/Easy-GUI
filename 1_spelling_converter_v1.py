""" A program that gets a NZ English word and converts it to US spelling"""

import easygui

nz_word = easygui.enterbox("Enter NZ English word", "NZ")
letters = list(nz_word)
letters.remove("u")

us_word = "".join(letters)
easygui.msgbox(f"The US spelling for {nz_word} is {us_word}", "US")
