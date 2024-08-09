set1 = {1, 2, 3, 5, 7, 9, (1, 2, 3, 4)}
set2 = {3, 4, 5, 9, (1, 2, 3)}
union_set = set1.union(set2)
print(union_set)


intersection_set = set1.intersection(set2)
print(intersection_set)

difference_set = set1.difference(set2)
print(difference_set)

input_list = [3, 66, 8.9, 'rt', 55, 3, 'rt', 'ttt', 55, 8.9, 0, 3, 5, 'rt', 3, 33]

result_list = []
for item in input_list:
    if item not in result_list:
        result_list.append(item)
print(result_list)

result_list_2 = list(set(input_list))
print(result_list_2)
