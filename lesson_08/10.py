def example_function(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


args = (1, 2, 3)
example_function(*args)


def example_function(a, b, c):
    print(a, b, c)


kwargs = {'a': 1, 'b': 2, 'c': 3}
example_function(**kwargs)  # ->  example_function(a=1, b=2, c=3)
