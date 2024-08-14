def my_func(item):
    print('id item:', id(item))
    item.append(5)
    print('item:', item)
    print('id item:', id(item))


a = [1, 2, 3]
print('a:', a)
print('id a:', id(a))

my_func(a[:])
print('a:', a)
