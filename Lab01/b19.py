
def new_string(text):
  # kiểm tra xem chuỗi text có dài ít nhất hai ký tự và có bắt đầu bằng “Is” hay không
  if len(text) >= 2 and text [:2] == "Is":
    return text
  return "Is" + text
print(new_string("Array"))
print(new_string("IsEmpty")) 
