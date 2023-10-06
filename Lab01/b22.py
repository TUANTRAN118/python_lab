# tim so 2 trong mang xuat hien may lan
def list_count_2(nums):
  count = 0  
  for num in nums:
    if num == 2:
      count = count + 1
  return count    

print(list_count_2([1, 2, 6, 7, 2]))
print(list_count_2([2, 4, 2, 4, 7, 2,3,2]))