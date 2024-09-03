class Woman:
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight - 5

    def __my_method(self):
        ...


a = Woman('Jessy', 27, 62)
print(a.name)
print(a._age)
# print(a.__weight)
print(a.get_weight())
print(a._Woman__weight)
