a = [1, 34, 66.7, 'eret', 2345, 'FRG', '0']

summa = 0
a_new = []
for item in a:
    if isinstance(item, (int, float)):
        summa += item
        if item % 5 != 0:
            a_new.append(item)

print('summa:', summa)
print('a_new:', a_new)
