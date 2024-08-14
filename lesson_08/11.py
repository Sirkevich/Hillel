def my_func(item):
    print('id item:', id(item))
    item += 1
    print('item:', item)
    print('id item:', id(item))


a = 10
print('a:', a)
print('id a:', id(a))

my_func(a)
print('a:', a)
