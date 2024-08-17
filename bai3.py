#bai3
a = float(input('Nhập a = '))
b = float(input('Nhập b = '))
c = float(input('Nhập c = '))
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Vậy a, b, c là 3 cạnh của tam giác')
    if a*a == b*b + c*c or b*b + a*a == c*c or c*c == a*a + b*b:
        print('Đây là tam giác vuông')
    elif (a == b) and (b == c):
        print('Đây là tam giác đều')
    elif a == b or a == c or b == c:
        print('Đây là tam giác cân')
    else:
        print('Đây là tam giác thường')
else: 
    print('Vậy a, b, c không là 3 cạnh của tam giác')
    
