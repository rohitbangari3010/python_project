import ceaser
print(ceaser.caesar_art)


alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser_cipher(user_choice,user_word,user_shift):
    new_word=[]
    len_alphabets=len(alphabets)
    for i in user_word:
        if i in alphabets:
            index=alphabets.index(i)
            if user_choice.lower()=='unicode':
                index_shift=index+user_shift
        
            elif user_choice.lower()=='decode':
                index_shift=index-user_shift
            
            else:
                print("please select one out of unicode or decode")
                ceaser_cipher()
            actual_shift=index_shift%len_alphabets
            decode_unicode=alphabets[actual_shift]
            new_word.append(decode_unicode)
        

        else:
            new_word.append(i)
    new_word=''.join(new_word)
    print(f"{user_choice}d word is {new_word}")


continue_game=True

while continue_game:
    user_choice=input("Do you want to decode or unicode ?")
    user_word=input("Type your message ?")
    user_shift=int(input("Type your shifts ?"))
    ceaser_cipher(user_choice,user_word,user_shift)
    user_continue=input("Do you want to start again yes or no \n")

    if user_continue=='no':
        continue_game=False


