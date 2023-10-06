from math import pi
import math


def DienTich(r):
    s = pi * math.pow(r,r)
    return s


r = float(input('Nhap ban kinh hinh tron : '))
s = DienTich(r)

while r <= 0: 
    print(f'ban kinh =  {r}  khong hop le ! \nvui long nhap lai ')
    r = float(input('Nhap ban kinh hinh tron : '))


print(f'ban kinh:  {r} có dien tich: {s}' )
