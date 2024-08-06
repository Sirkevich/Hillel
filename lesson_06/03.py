import copy

a = (1, 4, 'rrt', [3, 4, 5])
b = (1, 4, 'rrt', [3, 4, 5])

print(id(a))
print(id(b))

c = a[:]

print(c)
print(id(c))

d = copy.copy(a)
print(d)
print(id(d))

e = copy.deepcopy(a)
print(e)
print(id(e))
