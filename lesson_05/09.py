a = 'Simple text'
b = 'Simple tеxt'
c = 'Євген'

print(a.encode())
print(b.encode())
print(c.encode())

c_1 = c.encode()
print(type(c_1))
print(c_1)

c_2 = c_1.decode()
print(type(c_2))
print(c_2)
print(c_1.decode('Latin-1'))
