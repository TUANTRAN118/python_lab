# xuất tất cả số nguyên trong 1 khoàng cho trước
import math


a = int(input('Nhap vao so a: '))
b = int(input('Nhap vao so b: '))


def isPrime(num:int):
    if num <=1:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

def XuatSoNguyen(a,b:int):
     for i in range(a,b + 1):
        if i > 1:
            check = True
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    check = False
                    break
            if check:
                print(i, ' ')

        else:
            print(i, ' ')



while True:
    if isPrime(a) and isPrime(b) == True:
        print('Xuat so nguyen to :')
        XuatSoNguyen(a,b)
        break
    elif a > b:
        print('Số đầu lớn hơn số cuối, Lỗi !, vui lòng nhập lại')
        a = int(input('Nhap vao so a: '))
        b = int(input('Nhap vao so b: '))
    else:
        print('Số vừa nhập không phải số nguyên tố! vui lòng nhập lại')
        a = int(input('Nhap vao so a: '))
        b = int(input('Nhap vao so b: '))


