def summa(a, b):
    res = None
    if type(a) == int and type(b) == int:
        if a > b:
            res = a - b
        else:
            res = b - a
    elif type(a) == str and type(b) == str:
        res = a + b
    print(res)

    return res


def my_func():
    print('-' * 50)


def my_func_2():
    return 12, 13, 14


def my_func_3():
    return {a: 12, b: 34}


...
a = 10
b = 50
r = summa(a, b)
print(r)
...
c = 99
d = 66
summa(c, d)
my_func()
...
a = 'Hello'
b = ' world'
summa(a, b)
...
summa(77, 55)
...
my_func()

x, y, z = my_func_2()
print(x)
print(y)
print(z)

q = my_func_2()
print(q)
