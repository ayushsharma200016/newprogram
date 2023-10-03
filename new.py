import random
player1 = int(input('enter the integer valueuntill 100'))
computer = random.randint(0,100)
if player1 == computer:
    print('congratulations you guessed it right')
else:
    print('sorry try again')

