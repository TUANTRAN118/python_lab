import math

# các số nguyên + từ 1 -> n
# 1! = 1 and 0! = 1
#  5! = 5x4x3x2

#c1
def factorial(num:int):
    fact:int = 1
    if num == 0 or num ==1:
        return fact
    else:
        for i in range(2, num + 1):
            fact *=i 
        return fact

#c2
def factorial_2(num:int):
    fact:int =1
    if num == 0 or num ==1:
        return fact
    else:
        for i in reversed(range(2, num +1)):  # dao nguoc num+1 va 2
            fact *=i 
        return fact
    
#c3 dequi
def factorial_3(num:int):
    if num == 0:
        return 1
    return num * factorial_3(num -1) # (num-1)*(num-2)  (num-2)*(num-3)



print('Nhập vào 1 số nguyên dương bất kỳ để tính giai thừa')
while True:
    try:
        number = int(input('Nhập số nguyên dương: '))
        if number > 0 and isinstance(number, int):
            giaiThua = factorial_3(number)
            print(f'Số vừa nhập {number}! có kết quả là: ',giaiThua)
        else:
            print('Số vừa nhập không phải là số nguyên dương, vui lòng nhập lại !')  
    except ValueError:
        print('Số vừa nhập không phải là kí tự, vui lòng nhập lại !')











        

    

    















