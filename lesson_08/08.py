def my_func(a, b, *args, c=0, **kwargs):
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'c: {c}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    print('-' * 50)


my_func(1, 4, 55, 6, 4, c='ertre', d='44')
