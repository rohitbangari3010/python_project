print("""
        ____________________
       /__________________/|
      |  💰  TREASURE 💰  ||
      |   GOLD  DIAMOND   ||
      |__________________|/
""")

print("""Welcome to Treasure Island.  
Your mission is to find the treasure.
""")

print("You are at a cross road where do you want to go ?")
choice1=input("Do you wanna go left or right ? \n")

if choice1=='left':
    print("you are beside river")
    choice2=input("Do you wanna Swim or Wait here for some time ?")
    if choice2=="Wait":
        print("Thanks for waiting, doors has appeared.")
        choice3=input("""Please choose one door
                      Red Blue Yellow Black \n""")
        if choice3=="Yellow":
            print("Congrats, you win")
        elif choice3=="Red":
            print("""Burnt by fire
                  Game Over""")
        elif choice3=="Blue":
            print("""Eaten by a beast
                  Game Over""")   
        else:
            print("Game Over")
    else:
        print("Attacked by a trout, Game over")
else:
    print("Fall into a hole Game over")

