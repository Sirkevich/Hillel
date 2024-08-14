def my_func(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    print('-' * 50)


my_func()
my_func(1)
my_func(1, 4, 'ertre')
my_func(1, a=4, c='ertre')
my_func(a=4, b='2')
