import easygui

places = easygui.enterbox("Enter the names of 5 places you would most like to "
                          "visit\n Separate each place name with a comma",
                          "Enter favourite places")

places_list = places.split(",")

while len(places_list) > 5:
    easygui.msgbox(f"Sorry but you can only enter the names of 5 places and "
                   f"you entered {len(places_list)} places", "Too many places")

    places = easygui.enterbox("Enter the names of 5 places you would most like to "
                              "visit\n Separate each place name with a comma",
                              "Enter favourite places")

while len(places_list) < 5:
    easygui.msgbox(f"Sorry but you must enter at least 5 places and you only "
                   f"entered {len(places_list)}", "Not enough places")
    places_list = places.split(",")

    places = easygui.enterbox("Enter the names of 5 places you would most like to "
                              "visit\n Separate each place name with a comma",
                              "Enter favourite places")
    places_list = places.split(",")

easygui.msgbox(f"My bucket list \n\n")
for place in places_list:
    output = f"\n*    ".join(places_list)

easygui.msgbox(f"My bucket list: \n\n*    {output}", "Travel bucket list")
