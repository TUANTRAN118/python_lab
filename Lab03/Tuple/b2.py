Tuple1 = (2,'hihi', 3, 'haha', 5)
print(f"\nTuple với nhiều kiểu dữ liệu :{Tuple1}")

# nested tuple
Tuple1= (0,2,4,6)
Tuple2= ('zero, two, four, six')
Tuple3= (Tuple1,Tuple2)
print(f'\nGộp Tuple: {Tuple3}')

# repetition
Tuple1 = ('hihi',)*5
print(f"\nLặp Tuple 5 lần : {Tuple1}")


# tuple with loop
Tuple1 = ('hihi')
n=6
print("\nTuple voi vong lap")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)
