import easygui, random

word = "supercalifragilisticexpialidocious"
for i in range(20):
    letter = random.choice(word)
    easygui.msgbox(letter, f"Letter {i-1} chosen")
