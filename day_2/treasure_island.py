print("""
Welcome to Treasure Island.
Your mission is to find the treasure.
""")

direction = input("Do you want to go left or right? ")
if direction == "left":
    want_swim = input("Do you want to swim or wait? ")
    if want_swim == "swim":
        print("Attacked by trout. Game Over")
    else:
        which_door = input("Which door do you want to select (Red, Blue or Yellow)? ")
        if which_door == "red":
            print("Burned by fire. Game Over.")
        elif which_door == "blue":
            print("Eaten by beast. Game Over.")
        elif which_door == "yellow":
            print("You win!")
        else:
            print("Game Over.")
else:
    print("Fall into a hole. Game Over.")