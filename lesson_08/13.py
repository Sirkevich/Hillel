def my_func(a=None):
    if a is None:
        a = [0, 0, 0]
    a.append(len(a))
    return a


a_1 = []
a_1 = my_func(a_1)
print(a_1)

a_2 = [10,]
a_2 = my_func(a_2)
print(a_2)

a_4 = my_func()
print(a_4)

a_3 = [1, 5, 6]
a_3 = my_func(a_3)
print(a_3)

a_5 = my_func()
print(a_5)

a_6 = my_func()
print(a_6)
