a = [1, 34, 66.7, 'eret', 2345, 'FRG', '0']

a_new = []
for item in a:
    if isinstance(item, str):
        a_new.append(a)
    a.append(item)

print(a_new)
