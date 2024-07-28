import copy

a = [34, 66, True, 'rtre', 0.12, ['a', 'f', 77], None, 22, 99, 17]

if 'a' in a:
    print('YES')
else:
    print('NO')

# b = a
# c = a
# b = a[:]
# c = a[:]
b = copy.copy(a)
c = copy.copy(a)

b.pop()
c.insert(0, 22)

print(a)
print(id(a))
print(b)
print(id(b))
print(c)
print(id(c))

d = copy.deepcopy(a)
print(d)
print(id(d))

d[5].append(0)
print(d)
print(a)
print(b)
print(c)
