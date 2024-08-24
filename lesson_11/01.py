file = open('test.txt', 'w', encoding='utf-8')
file.write('Привіт всесвіт!')
file.close()

file = open('test.txt', encoding='utf-8')
text_1 = file.read()
file.close()

with open('test.txt', 'rb') as file:
    text_2 = file.read()

print(f'text_1: {text_1}')
print(type(text_1))
print(f'text_2: {text_2}')
print(type(text_2))

print(text_2.decode('utf-8'))
