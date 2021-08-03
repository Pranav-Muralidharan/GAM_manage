import random

print('guess the number(0 to 100)')

number=random.randint(0,100)
chance=0
a=False

while not a:
    guess=int(input("Guess the no: "))
    chance+=1
    if guess==number:
        a=True
        print(f'You Won!!!...taken {chance} chances')
    elif guess>number:
        print(f'actual number is less than {guess}')
    else:
        print(f'actual number is greater than {guess}')
