a = [34, 66, True, 'rtre', 0.12, [1, 11, 34, 100, 44, 0, 56], None, 22, 99, 17]

b = a[1:5]
print(b)
print(a)

# c = a[0:100]
# c = a[0:]
c = a[:]
print(c)

print(id(a))
print(id(c))

s = a[:3]
print(s)

d = a[-1:-4:-1]
print(d)

q = a[:-1:3]
print(q)

print(a[5][-1::-2])
print(a[-1::-1])
