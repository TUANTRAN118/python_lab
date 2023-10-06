# kiểm tra n có nằm trong mảng hay không

def check_list(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(check_list([1, 5, 8, 3], 3))
print(check_list([5, 8, 3], 4))
