def my_decorator(func):
    def wraper():
        print('Before function')
        func()
        print('After function')

    return wraper


@my_decorator
def my_func():
    print('I am alone function')


@my_decorator
def my_func1():
    print('I am a first function')


@my_decorator
def my_func2():
    print('I am a second function')


my_func()
print('-' * 50)
my_func1()
print('-' * 50)
my_func2()
