a = {1, 0, 2, 'rt', 99, True}

b = {4, 'world', 99, 'rt', (3, 4, 66, 77)}
c = [4, 'world', 99, 'rt', (3, 4, 66, 77)]

print(a)
print(b)

a.remove(99)
print(a)

a.discard(99)
print(a)
