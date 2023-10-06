import math


a = float(input('Nhap vao so a : '))
b = float(input('Nhap vao so b : '))

def TinhTong(a, b):
    sum = a + b
    return sum

def TinhThuog(a,b):
    divide = a/b
    return divide

def TinhBinhPhuong(a,b):
    BinhPhuong = math.pow(a,b)
    return BinhPhuong


tong = TinhTong(a,b)
chia = TinhThuog(a,b)
binhPhuong = TinhBinhPhuong(a,b)

print(f'{a} + {b} = {tong}')
print(f'{a} / {b} = {chia}')
print(f'{a} ^ {b} = {binhPhuong}')