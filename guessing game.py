# Guessing the number in three attempts

import random
fix= random.randint(1,10)
def guessgame():
    for attempts in range(1,4) :
        choice=int(input('Guess a number:'))
        if choice==fix:
            print('Correct Guess')
            break
        else:
            print('Wrong Guess')
        if attempts>=3 and choice!=fix:
            print('You lost the game .\n Game Over ')

guessgame()
ch=input(' you want to play again? Y/N:')
if ch=='y':
    guessgame()
elif ch=='n':
    print('THANK YOU')
elif ch != 'y'or'n':
    print('choose correct option')
