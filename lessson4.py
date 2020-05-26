# -*- coding: utf-8 -*-
import random
a=random.randint(1,30)

while True:
    guess=int(input('guess1-20:'))
    if guess==a:
        print('bingo')
        break
    elif guess>a:
        print('too big','smaller')
    elif guess<a:
        print('too small','bigger')
            






























