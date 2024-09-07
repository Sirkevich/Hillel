class People:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.second_name}'

    @full_name.setter
    def full_name(self, new_value):
        self.first_name, self.second_name = new_value.split()

    @full_name.deleter
    def full_name(self):
        del self.first_name
        del self.second_name


a_1 = People('Bob', 'Red')
print(a_1.__dict__)

a_1.second_name = 'White'
print(a_1.__dict__)
print(a_1.first_name)
print(a_1.second_name)
print(a_1.full_name)

print('-' * 50)

a_1.full_name = 'Jack Smith'
print(a_1.first_name)
print(a_1.second_name)
print(a_1.full_name)

print('-' * 50)

del a_1.full_name
print(a_1.__dict__)

