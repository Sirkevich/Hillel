def my_func(type=1):
    def func_1(a='hello'):
        return a.title()

    def func_2(a='buy'):
        return a + '!'

    if type == 1:
        return func_1
    else:
        return func_2


print(my_func(4)('Sasha'))
