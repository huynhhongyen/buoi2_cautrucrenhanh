#cach1
dis = int(input('Quãng đường đi được là: '))
if dis == 1:
    tien = 20000
elif dis == 2:
    tien = 2*13000
elif dis == 3:
    tien = 3*13000
elif 4 <= dis <= 8:
    tien = 3*13000 + (dis - 3)*12000
else: 
    tien = 3*13000 + (8 - 3)*12000 + (dis - 8)*10000
if tien > 100000:
    tien = tien*0.92
print('Tiền taxi là:',tien)

