# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:40:43 2024

@author: ASUS
"""

print('Nhập ngày, tháng, năm:')
day = input()
month = input()
year = int(input())
date = f'{day}/{month}/{year}'
print(date)

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year,'là năm nhuận')
else: 
    print(year,'không là năm nhuận.')
if month == "4" or month == "6" or month == "9" or month == "11":
        print('Tháng',month,'có 30 ngày')
elif month == "2":
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Tháng 2 có 29 ngày')
    else: print('Tháng 2 có 28 ngày')
else: 
    print('Tháng',month,'có 31 ngày')