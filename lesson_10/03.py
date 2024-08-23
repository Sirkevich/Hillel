def my_decorator(func):
    def wraper():
        print('Before function')
        func()
        print('After function')

    return wraper


def my_func():
    print('I am alone function')


my_func()
print('-' * 50)
my_func = my_decorator(my_func)
my_func()
