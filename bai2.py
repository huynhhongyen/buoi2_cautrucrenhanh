#bai2.1
a = float(input('Nhậ­p a = '))
b = float(input('Nhậ­p b = '))
if a == 0:
   print('Phương trình vô nghiệm')
else:
    print('Phương trình có nghiệm là: ',-b/a)
    
#bai2.2
a = float(input('Nhậ­p a = '))
b = float(input('Nhậ­p b = '))
c = float(input('Nhậ­p c = '))
if a == 0:
    if b == 0:
        print('Phương trình vô nghiệm')
    else:
        print('Phương trình có nghiệm là: ',-b/a)
else: 
    delta = b**2 - 4*a*c   
    if delta > 0:
        import math
        print('Phương trình có 2 nghiệm phân biệt là: ',(-((b) + math.sqrt(delta))/(2*a)),',', (-((b) - math.sqrt(delta))/(2*a)))

    elif delta == 0:
        print('Phương trình có nghiệm kép là: ',(-(b)/2*a))

    else:
        print('Phương trình vô nghiệm')


















