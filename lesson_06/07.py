from collections import namedtuple

Point = namedtuple('Point', 'x y')

# Створюємо екземпляр Point з координатами (1, 2)
p = Point(1, 2)

a_1 = (3, 5)
a_2 = (-4, 0)
a_3 = (10, 10)

for point in (a_1, a_2, a_3):
    print(point[0])


print('-' * 100)
b_1 = Point(3, 5)
b_2 = Point(-4, 0)
b_3 = Point(10, 10)

for point in (b_1, b_2, b_3):
    print(point.x)
    print(point[0])

print(b_2.x)
print(b_2[0])
