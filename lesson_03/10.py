a = [34, 66, True, 'rtre', 0.12, None, 22, 99, 17]
b = ['a', 'f', 77]

print(a)

a.append(0)
print(a)

print(len(a))
a.insert(3, [1, 2, 3])
print(a)
print(len(a))

a[1] = 88
print(a)

a.extend(b)
print(a)

c = a.pop()
print(a)
print(c)

d = a.pop(3)
print(a)
print(d)

del a[-2]
print(a)

w = a.remove(99)
print(a)
print(w)

a.reverse()
print(a)
print(b)
