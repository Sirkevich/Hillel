def my_func(c=0, a=0, b=0, **kwargs):
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'c: {c}')
    print(f'kwargs: {kwargs}')
    print(len(kwargs))
    print('-' * 50)


a = 10
b = 5
my_func(c=11, b=a, a=b, d=77, e=34, z=12)
my_func()
my_func(c=11, d=77)
