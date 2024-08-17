GPA = float(input('Nhập điểm trung bình: '))
if GPA < 3.5:
    print('Học lực kém')
elif 3.5 <= GPA < 5.0:
    print('Học lực yếu')
elif 5.0 <= GPA < 7.0:
    print('Học lực trung bình')
elif 7.0 <= GPA < 8.0:
    print('Học lực khá')
elif 8.0 <= GPA < 9.0:
    print('Học lực giỏi')
else:
    print('Học lực xuất sắc')
    