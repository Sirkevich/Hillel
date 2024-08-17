def calculate_area(radius: (int, float), a: list = [0]) -> str:
    area = radius + a[0]
    # area = 3.14 * radius ** 2
    return area


print(calculate_area(55, [1, 2, 3]))
# print(calculate_area.__doc__)
print(calculate_area.__annotations__)
