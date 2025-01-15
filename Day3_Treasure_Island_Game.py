print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# This project utilized the nested if-elif-else structure

# Choice 1 using the .lower() appended
choice1 = input("You're at a cross road. Where do you want to go?\n Type \"left\" or \"right\"\n").lower()
if choice1 == "left":
    choice2 = input("Great choice, you must have noticed the hole to the right.\n "
          "So now you happen upon a lake. And you notice there is an island in the middle of the lake. "
          "What do you do?\n Type \"wait\" to wait for a boat or \"swim\" to try and swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You find a boat, and you take it."
              "And now you arrive at the island unharmed. ***phew***"
              "Then you come across a house with 3 doors, all different colors.\n"
              "The colors are red, blue and yellow. Which door do you choose?\n").lower()
        if choice3 == "red":
            print("You picked the fire door. You were consumed by hot flames instantly.\n Game Over.")
        elif choice3 == "blue":
            print("You picked the ice door. You were instantly turned into a giant block of ice.\n Game Over.")
        elif choice3 == "yellow":
            print("Congratulations, you picked the treasure door!\n You win the game!")
        else:
            print("You did not enter a valid choice, Game Over.")

    elif choice2 == "swim":
        print("Bad choice. You were eaten by a shark, ***nom nom nom***.")
        exit()
    else:
        print("You did not enter a valid choice, Game Over.")
        exit()

elif choice1 == "right":
    print("You fell in to a hole. Game Over.")
    exit(None)
else:
    print("You did not enter a valid choice, Game Over.")
    exit(None)
