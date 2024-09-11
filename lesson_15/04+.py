class People:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.__age = age

    def __iter__(self):
        pass

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 0 <= new_age < 100 and new_age > self.__age:
            self.__age = new_age


a_1 = People('Bob', 'Red', 5)
print(a_1.age)
a_1.age = 'dfgrgbf'
print(a_1.age)
a_1.age = 28
print(a_1.age)
a_1.age = 25
print(a_1.age)
a_1.age = 125
print(a_1.age)

for item in a_1:
    pass
