a = [34, 66, True, 'rtre', 0.12, None, 22, 99, 17]
b = a

a[2] = 100
print(a)

a[1:4] = 1, 2, 3, [55, 66, 77], 5
print(a)

a = []
# a.clear()
print(a)
print(b)
