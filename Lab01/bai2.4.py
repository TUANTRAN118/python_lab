# Kiểm tra n có phải số fibonacci k ?
import math


def isFibonacci(n: int):
    if n == 0 or n == 1:
        return True
    else:
        return (math.isqrt(5*pow(n, 2)+4))**2 == 5*pow(n, 2) + 4 or (math.isqrt(5*pow(n, 2)-4))**2 == 5*pow(n, 2) - 4


print('Nhập vào một số để kiểm tra có phải là số fibonacci hay không')
number = int(input('Nhập số : '))

while True:
    if (number < 0):
        print('số vừa nhập không hợp lệ, vui lòng nhập số khác !')
        number = int(input('Nhập số : '))
    else:
        break

while True:
    if (isFibonacci(number) == True):
        print(number, 'là số Fibonacci')
        break
    else:
        print(number, 'không là số Fibonacci, vui lòng nhập số khác !')
        number = int(input('Nhập số : '))



