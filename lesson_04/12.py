import random


data_list = [random.randint(1, 10) for i in range(random.randint(3, 10))]

print(data_list)

data_list_2 = []
for _ in range(random.randint(3, 10)):
    data_list_2.append(random.randint(1, 10))


my_list = [1, 55, 'sdg', '446', -12, 56.34, False]
new_list = [i + 2 if type(i) == int else i for i in my_list if type(i) != str]
new_list_3 = [i + 2 for i in my_list if type(i) == int]
print(new_list)
print(new_list_3)

new_list_2 = []
for i in my_list:
    if type(i) != str:
        new_list_2.append(i + 2 if type(i) == int else i)
print(new_list_2)
