import gamedata
import random

def highorlow(A,B):
    print(f'''{A["name"]} followers are {A["followers"]}\n {B["name"]} followers are {B["followers"]} ''')
    if A['followers']>B['followers']:
        
        return 1
    else:
        return 0

def remove_from_data(item):
    gamedata.data.remove(item)
    return 

A=random.choice(gamedata.data)
remove_from_data(A)


life=True
score=0


while life:
    if gamedata.data==[]:
        life=False
        print(f"congrats you completed the game with score {score}")
    else:
        B=random.choice(gamedata.data)
        remove_from_data(B)
        print(f'A-{A["name"]}\n B-{B["name"]}\n')
        player_choice=input("select A or B")
        if player_choice=="A":
            player_choice=A
            result=highorlow(player_choice,B)
        else:
            player_choice=B
            result=highorlow(player_choice,A)
        if result==1:
            A=player_choice
            score+=1
        else:
            life=False
            print(f"Game over\n your score is {score}")

