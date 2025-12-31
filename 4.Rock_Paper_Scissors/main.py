import random

Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images=[Rock,Paper,Scissors]

user_choice=int(input("Make your choice. " \
"0 - Rock " \
"1 - Paper " \
"2 - Scissors"))


computer_choice=random.randint(0,2)

print(f"""User Choice is
       {game_images[user_choice]}""")
print(f"""Computer choice is 
      {game_images[computer_choice]}""")


if user_choice==computer_choice:
    print("game ties")
elif user_choice>=3 and user_choice<0:
    print("Unavailable options, please select from 0 to 2 only")
elif user_choice==0 and computer_choice==2:
    print("user wins")
elif user_choice==2 and computer_choice==0:
    print("computer wins")
elif user_choice>computer_choice:
    print("user wins")
elif computer_choice>user_choice:
    print("computer wins")
