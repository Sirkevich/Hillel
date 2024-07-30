a = [1, 34, 66.7, 'eret', 2345, 'FRG', '0']

a_new = []
a_indexes = []
for index, item in enumerate(a):
    if isinstance(item, str):
        a_new.append(item)
        a_indexes.append(index)

print(a_new)
print(a_indexes)

a_new_2 = []
a_indexes_2 = []
for item in enumerate(a):
    if isinstance(item[1], str):
        a_new_2.append(item[1])
        a_indexes_2.append(item[0])

print(a_new_2)
print(a_indexes_2)
