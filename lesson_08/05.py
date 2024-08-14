def my_func(c, a=0, b=0):
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'c: {c}')
    print('-' * 50)


a = 10
b = 5
my_func(c=11, b=a, a=b)
my_func(a=b, c=11, b=a)
my_func(c=11, a=b, b=a)

my_func(34)
my_func(34, b=100)
my_func(34, 100)
