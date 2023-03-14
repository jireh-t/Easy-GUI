"""A program that helps Tama check if he's met his tech-free goal"""

import easygui

GOAL = 3

days_used = easygui.enterbox("Please enter each of the days on which you used "
                             "technology\n"
                             "Separate each day with a space", "Days tech was used")

days_free = 7 - len(days_used.split())

if days_free < GOAL:
    easygui.msgbox(f"Too bad! You had {days_free} tech-free days.\n"
                   f"That is {GOAL - days_free} less than your goal")

else:
    easygui.msgbox(f"Congratulations! You had {days_free} tech-free days.\n"
                   f"You met your goal of {GOAL} tech-free days.")
