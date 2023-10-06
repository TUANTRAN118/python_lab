#giải phương trình bậc 2
# Phương trình vô số nghiệm khi: hệ số a, b, c đều bằng 0
# Phương trình vô nghiệm khi: hệ số a, b bằng 0, c khác 0 và trường hợp delta nhỏ hơn 0
# Phương trình có nghiệm kép khi delta bằng 0
# Phương trình có hai nghiệm phân biệt khi delta lớn hơn 0

import math


def Delta(a,b,c:float):
    D = (b**2) - (4* a* c)
    return D


def GiaiPhuongTrinh(a,b,c:float):
    D = Delta(a,b,c)

    if(D < 0):
        return False # vo no
    
    elif(D == 0):
        x = (-b / (2*a))
        return x # no kep
    else:
        x2 = (-b + math.sqrt(D))/(2*a)
        x1 = (-b - math.sqrt(D))/(2*a)
        
        return x1,x2 # 2 no
    

while True: 
    try:
        a = float(input('Nhập số a : '))
        b = float(input('Nhập số b : '))
        c = float(input('Nhập số c : '))

        if a == 0:
            if b== 0:
                if c== 0:
                    print('Phương trình có vô số nghiệm !')
                else: 
                    print('Phương trình vô nghiệm !')
            else:
                print('Phương trình có 1 nghiệm duy nhất X = ',-c / b)

        else: 
            delta = Delta(a,b,c)  
            phuongTrinh = GiaiPhuongTrinh(a,b,c)
            if(delta < 0):
                print('Phương trình vô nghiệm !')
            elif(delta == 0):
                print('Phương trình có nghiệm kép X1 = X2 = ',phuongTrinh)
            else:
                X1, X2 = GiaiPhuongTrinh(a,b,c)
                print('Phương trình có 2 nghiệm phân biệt X1 = ',X1,' và X2 = ',X2)

    except ValueError:
        print('Bạn vừa nhập không phải số, vui lòng nhập lại !')



  







# def my_function():
#   a = 1; b=5
#   return a,b 

# a, b = my_function()
# print(a)
# print(b)