def func_2():
    print('Func 2')


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point: x={self.x}, y={self.y}'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


a = Point(5)
print(a)
b = Point(2, 4)
print(b)
c = a + b
print(c)
print(type(c))
