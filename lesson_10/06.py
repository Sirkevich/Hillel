def my_decorator(func):
    def wraper(*args, **kwargs):
        print('Before function')
        result = func(*args, **kwargs)
        print('After function')
        return result

    return wraper


@my_decorator
def my_func(name):
    return f'I am {name} function'


print(my_func('alone'))

