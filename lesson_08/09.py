def example_function(positional_arg, *args, **kwargs):
    print("Positional Arg:", positional_arg)
    print("Additional Positional Args:", args)
    print("Additional Named Args:", kwargs)


def example_function_with_named_arg(named_arg):
    print("Named Arg:", named_arg)


# Виклик функції з використанням різних видів аргументів
example_function(1, *range(3, 6), keyword_arg="value")

# Виклик функції з використанням іменованих аргументів
example_function_with_named_arg(named_arg=2)
example_function(1, 3, 4, 5, named_arg=2, keyword_arg="value")
