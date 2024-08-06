japan_str = 'ぁぃえおき'
japan_char = '㍿'
name = 'Tom'
word = 'ciào'
surname = 'Арефа'


japan_char_byte = japan_char.encode("utf-8")
japan_char_byte_2 = japan_char.encode("utf-16")
print(japan_char)
print(japan_char_byte)
print(type(japan_char_byte))
print(japan_char_byte_2)
print(japan_char_byte_2.decode("windows-1251"))

print(japan_str.encode())
print(len(japan_str.encode()))

print('-' * 100)
print(surname.encode())
print(len(surname.encode()))

print('-' * 100)
print(name.encode())
print(len(name.encode()))

print('-' * 100)
print(word.encode())
print(len(word.encode()))

print('-' * 100)
print(word.encode().decode("latin-1"))
