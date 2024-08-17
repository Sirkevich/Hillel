a = 100
b = False if a > 100 else True

c = [i**2 for i in range(a)]


def square(x, y):
    sum = x * y
    return sum


square_2 = lambda x, y: x * y


print(square(3, 4))
print(square_2(3, 4))
