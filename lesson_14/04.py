from lesson_13.hw_01 import Human


class SuperHuman(Human):
    def __eq__(self, other):
        return self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __float__(self):
        if self.gender == 'FeMale':
            res = self.age - 5
        else:
            res = self.age + 1
        return float(res)


def func_3(self):
    print('FUNC 3')


Human.new_func = func_3


a_1 = SuperHuman('Male', 33, 'Bob', 'White')
a_2 = SuperHuman('FeMale', 12, 'Kate', 'King')
a_3 = SuperHuman('Male', 12, 'Jack', 'Dow')

print(a_1 == a_3)
print(a_1 != a_3)
print(a_2 == a_3)

print(a_1 > a_3)
print(a_1 < a_3)

print('-' * 50)
print(a_2 > a_3)
print(a_2 < a_3)

print(float(a_2))

b_1 = Human('Male', 23, 'Bob', 'White')
b_1.new_func()
