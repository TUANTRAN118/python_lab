def larger_string(text, n):
   result = "|"
   for i in range(n):
      result = result + text
   return result

print(larger_string('aaa', 3))
print(larger_string('0.0.0', 3)) 
