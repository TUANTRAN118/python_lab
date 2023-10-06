def tong_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    sum = 1 
    a = 0 
    b = 1  

    for i in range(2, n):
        c = a + b
        sum += c
        a, b = b, c
    return sum

n = int(input("Nhập số n: "))
if n < 0:
    print("Vui lòng nhập số không âm")
else:
    kq = tong_fibonacci(n)
    print("Tổng của", n, "số Fibonacci đầu tiên là:", kq)
