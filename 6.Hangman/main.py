stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
]

import random

words=['Rohit','King','Giritra','harshit','Alok','Kailash','Rohan']


random_word=random.choice(words)
blanks=[]
for i in range(len(random_word)):
    blanks.append('_')



lives=6

while lives>0 and '_' in blanks:
    user_guess=input('Guess a word')

    if user_guess in random_word :
        for i in range(len(random_word)):
            if random_word[i]==user_guess:
                blanks[i]=user_guess

        new_blanks=''.join(blanks)
        print(new_blanks)
    else:
        
        print(stages[6-lives])
        lives-=1
        print(f'remaining lives {lives}')

if lives==0:
    print(stages[6-lives])
    print("Game Over, You Loose")

else:
    print("congrats, you won")





