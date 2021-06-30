import random
import os
import time

letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
simon= ""

for score in range(0,100):
    simon += random.choice(letters)
    for letter in simon:
        print(f'letter : {letter}')
        time.sleep(1.5)
        os.system("cls")
    guess=input("repeat all= ")
    os.system("cls")
    if guess!=simon:
        break

print(f'Game Over :) score={score}!')