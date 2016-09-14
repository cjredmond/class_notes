for _ in range(5):
    print("I am looping")

turns = 0
while turns < 5:
    print("WHILE LOOPING")
    turns = turns + 1
choice = ""
while choice != "n":
    choice = input("Do you want to loop again? [Y/n] ")
