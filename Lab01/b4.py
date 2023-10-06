from math import pi


def DienTich(r):
    s = 2*pi*r
    return s


r = float(input('Nhap ban kinh hinh tron : '))
s = DienTich(r)
while r > 0: 
	print(f'ban kinh =  {r} nhap vao khong hop le !vui long nhap lai ')


print(f'ban kinh:  {r} có dien tich: {s}' )








        
	