a = [34, 66, True, 'rtre', 0.12, [1, 11, 100], None]

print(a[0])
print(a[-2])
print(a[-2][-1])

element = a[-2]
if type(element) == list:
    print(element[0])

print(a[-2][0]) if type(a[-2]) is list or type(a[-2]) is tuple else print(a[-2])
print(a[-2][0]) if isinstance(a[-2], (list, tuple)) else print(a[-2])
