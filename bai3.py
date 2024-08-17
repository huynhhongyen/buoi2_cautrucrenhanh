#bai3
a = float(input('Nhậ­p a = '))
b = float(input('Nhậ­p b = '))
c = float(input('Nhậ­p c = '))
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Vậy a, b, c là  3 cạnh của tam giác')
    if a*a == b*b + c*c or b*b + a*a == c*c or c*c == a*a + b*b:
        print('Đây là tam giác vuông')
    elif (a == b) and (b == c):
        print('Đây là tam giác đều')
    elif a == b or a == c or b == c:
        print('Đây là tam giác cân')
    else:
        print('Đây là tam giác thường')
else: 
    print('Vậy a, b, c không là  3 cạnh của tam giác')
    
