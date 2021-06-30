import random

hand=['stone','paper','scissor']
com=0
player=0

print('Stone_Paper_Scissor \n 5 point to win')

while player<5 and com<5:
    opt=random.choice(hand)
    our_opt=input('stone/paper/scissor: ')
    if our_opt.lower()==opt:
        print('tie &!')
    elif our_opt.lower()=='stone':
        if opt=='paper':
            com+=1
            print(f'com wins..\n com:{opt} ; player:{our_opt}')
        elif opt=='scissor':
            player+=1
            print(f'player wins..\n com:{opt} ; player:{our_opt}')
    elif our_opt.lower()=='paper':
        if opt=='stone':
            player+=1
            print(f'player wins..\n com:{opt} ; player:{our_opt}')
        elif opt=='scissor':
            com+=1
            print(f'com wins..\n com:{opt} ; player:{our_opt}')
    elif our_opt.lower()=='scissor':
        if opt=='stone':
            com+=1
            print(f'com wins..\n com:{opt} ; player:{our_opt}')
        elif opt=='paper':
            player+=1
            print(f'player wins..\n com:{opt} ; player:{our_opt}')
    else:
        print('ERROR!!!')
print('Player wins the match :)' if player>com else 'Com wins the match :)')
