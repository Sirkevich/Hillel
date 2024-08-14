def my_func(a, b=99, *args):
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'args: {args}')
    print('-' * 50)


a = 10
b = 5
my_func(b, 0, a)
my_func(b, 0)
my_func(b, 0, 1, 2, 100, 101, 1110)
my_func(11)
