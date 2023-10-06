a = int(input("Input an integer : "))
# % định dạng dạng chuỗi 
# gán n1 là giá trị số nguyên của biến a
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a,) )
n4 = n1+n2+n3
print(n4)


