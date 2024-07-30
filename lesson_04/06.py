a = [1, 34, 667, 'eret', 2345, 'FRG', '0']

s = 0
i = 0
while i < len(a):
    if type(a[i]) == int:
        s += a[i]
    i += 1
print(s)

s_2 = 0
# item = a[0]
# item = a[-1]
for item in a:
    if type(item) == int:
        s_2 += item
print(s_2)
print(item)


count = 0
for _ in a:
    count += 1
print(count)


for item in a:
    ...
