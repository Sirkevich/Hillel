def my_func():
    print('Hello, world')


my_func()
print(my_func)

b = my_func
b()
del my_func
b()


def my_func_2():
    def say(name='Nobody'):
        print(f'Hello, {name}')

    return say


new_func = my_func_2()
new_func('Jack')
