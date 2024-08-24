with open('file_1.txt', 'wb') as f:
    f.write('Hello, world'.encode())

with open('file_2.txt', 'w') as f:
    f.write('Hello, world\nSecond line\nLast\tline\n')


file = open('file_2.txt', 'rb')
try:
    text = file.read().decode()
finally:
    file.close()

print(text)


file = open('file_2.txt')
try:
    text_2 = file.readline().strip()
    text_3 = file.readline().strip()
finally:
    file.close()

print(text_2)
print(text_3)


file = open('file_2.txt')
try:
    text_all = file.readlines()
finally:
    file.close()

print(text_all)
