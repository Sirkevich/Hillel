def my_decorator(func):
    def wraper(*args, **kwargs):
        print('Before function')
        func(*args, **kwargs)
        print('After function')

    return wraper


@my_decorator
def my_func():
    print('I am alone function')


@my_decorator
def my_func1(a='first'):
    print(f'I am a {a} function')


@my_decorator
def my_func2(a, c):
    print(f'I am a {a} {c}')


my_func()
print('-' * 50)
my_func1()
print('-' * 50)
my_func1('Top')
print('-' * 50)
my_func2('second', 'function')
