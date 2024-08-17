# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:58:36 2024

@author: ASUS
"""

import random
player = input('Bạn chọn gì (kéo, búa, bao)?: ')
com = random.choice(['kéo','búa','bao'])
print('Máy chọn:',com)
if player == com:
    print('Hòa')
elif player == "kéo" and com == "búa" or player == "búa" and com == "bao" or player == "bao" and com == "kéo":
    print('Bạn thua rồi.')
else: 
    print('Bạn thắng rồi.')

