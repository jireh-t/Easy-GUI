import easygui
import random

player = 0

for roll in range(2):
    player += 1
    num = random.randint(1, 6)
    num2 = random.randint(1, 6)

    easygui.msgbox(f"Player {player} you rolled:\n\n"
                        f"{num} and {num2}\n\n"
                        f"Total: {num + num2}", f"Player {player}")
