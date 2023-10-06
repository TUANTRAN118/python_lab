# chuyền vào 1 ký tự, kiểm tra kí tự đó có trong all_vovels thay không

def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))
print(is_vowel('io'))
