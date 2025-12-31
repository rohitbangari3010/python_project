import random

alphabets = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

usr_letters=int(input("how many letters do you want in your password ?"))
usr_numbers=int(input("how many numbers do you want ?"))
usr_symbols=int(input("how many symbols do you want ?"))

password=[]
for i in range(usr_letters):
    password.append(random.choice(alphabets))
for i in range(usr_numbers):
    password.append(random.choice(numbers))
for i in range(usr_symbols):
    password.append(random.choice(symbols))

print(password)
random.shuffle(password)

password=''.join(password)

print(f'your password is {password}')


