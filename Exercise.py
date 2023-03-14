import easygui, random

easygui.enterbox("Hi! What is your name? ")
easygui.integerbox("How old are you?", "Age")  # Don't need integer checker
easygui.buttonbox("Do you want to continue?", "Game Continue", choices=[
    "Yes", "No", "Maybe"])
easygui.msgbox("Kia ora! Welcome to EasyGui!")

# for i in range(100):
#     number = random.randint(0, 5)
#     print(number)

words = ["bat", "cat", "hat", "mat"]
my_word = random.choice(words)
print(my_word)


