a = [1, 34, 66.7, 'eret', 2345, 'FRG', '0']

a_new = []
a_indexes = []
index = 0
for item in a:
    if isinstance(item, str):
        a_new.append(item)
        a_indexes.append(index)
    index += 1

print(a_new)
print(a_indexes)
