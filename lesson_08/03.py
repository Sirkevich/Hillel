def my_func(a, b, c=99, d=55):
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'c: {c}')
    print(f'd: {d}')
    print('-' * 50)


a = 10
b = 5
my_func(b, 0, a)
my_func(b, 0)
my_func(b, 0, 1, 2)
