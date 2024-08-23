def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function


closure = outer_function(10)
closure_1 = outer_function(20)
result = closure(5)
print(result)

result = closure_1(5)
print(result)
