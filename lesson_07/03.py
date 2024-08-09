a = {1, 2, 4, 5, 99, 34, 23, 78, 90, 100, 45, 55}

input_list = [33, -23, 66, 45, 100, 90, 99, 2, 1]

for item in input_list:
    if item in a:
        ...

result = list(set(input_list).difference(a))
print(result)
