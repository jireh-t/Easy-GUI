import easygui

while True:
    school = easygui.enterbox("Enter the name of the school", "School name")
    max_num = easygui.integerbox("What is the maximum number of children allowed "
                                 "per class: Must be a number between 10 and 30",
                                 "Maximum class size", upperbound=30, lowerbound=10)

    total_children = easygui.integerbox(f"What is the number of children at "
                                        f"{school}: \n Must be a number between "
                                        f"10 "
                                        f"and 1400", "Total roll of school",
                                        upperbound=1400, lowerbound=10)

    classes = total_children // max_num

    teachers = easygui.integerbox(f"How many teachers at {school}:\n"
                                  f"Must be a number between 1 and 120",
                                  "Actual number of teachers",
                                  upperbound=120, lowerbound=1)

    if classes < teachers:
        easygui.msgbox(f"You have too many teachers. \n"
                       f"You could do without {teachers - classes} teachers",
                       "Over-staffed")
    elif classes > teachers:
        easygui.msgbox(f"You don't have enough teachers.\n"
                       f"You need {classes - teachers} more teachers",
                       "Under-staffed")

    elif classes == teachers:
        easygui.msgbox("You have the right amount of teachers", "Correctly "
                                                                "staffed")

    again = easygui.buttonbox("Do you want to perform another calculation?",
                              "More ratios?", choices=['Yes', 'No'])
    if again == "No":
        break
easygui.msgbox("Goodbye!", "Thanks for using this calculator")
