def calculate_area(radius):
    """
    Calculate the area of a circle.

    :param radius: The radius of the circle.
    :return: The area of the circle.
    """
    area = 3.14 * radius ** 2
    return area


# Виведення документації функції
print(calculate_area(5))
# print(help(calculate_area))
print(calculate_area.__doc__)
