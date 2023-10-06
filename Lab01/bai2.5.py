# tìm số fibonacci thứ n


#sử dụng vòng lặp 
def isFibonacci(n:int):
    f0 = 0
    f1 = 1
    fn = 1

    if n == 0 or n ==1:
        return n
    else:
        for i in range(2,n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn

# sử dụng đệ quy
# def isFibo(n):
#     if (n == 0 or n == 1):
#         return n
#     else:
#         return isFibo(n - 1) + isFibo(n - 2)



print('Nhập vào một số để tìm số fibonacci thứ n ')
number = int(input('Nhập số : '))

fibo = isFibonacci(number)
#fibo = isFibo(number)

while True:
    try:
        if (number < 0):
            print('số vừa nhập không hợp lệ, vui lòng nhập số khác !')
            number = int(input('Nhập số : '))
        else:
            print(fibo, 'là số fibonacci thứ ', number)
            break
    except ValueError:
        print('Giá trị nhập không hợp lệ !, nhập lại')



