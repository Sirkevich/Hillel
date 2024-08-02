b = 'helLo, WoRld!'
a = 'WO@RLD !'
c = '@##$%^T'
d = 'heLLo'

print(b.upper())
print(b.isupper())
print(a.isupper())
print(c.isupper())

print(b.lower())
print(a.title())
print(b.title())
print(b.capitalize())

print(d.title())
print(d.capitalize())

print('-' * 100)

print(d.ljust(10))
print(d.rjust(10))
print(d.center(10, '_'))
print(b.center(10, '_'))
