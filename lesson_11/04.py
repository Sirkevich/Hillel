file = open('test_2.txt', 'w', encoding='utf-8')
file.write('Привіт всесвіт!')
file.close()

file = open('test_2.txt', 'rb')
try:
    text = file.read(9)
finally:
    file.close()

print(text.decode('utf-8'))
