class Car(object):
    def __init__(self, model, number):
        self.model = model
        self.number = number

    def __str__(self):
        return f"Model: {self.model}, number: {self.number}"


class User:
    def __init__(self, name, surname, auto=None):
        self.name = name
        self.surname = surname
        if auto is None:
            self.auto = []
        else:
            if isinstance(auto, list):
                self.auto = auto
            else:
                self.auto = [auto,]

    def __str__(self):
        auto_str = [item.model for item in self.auto]
        is_auto = ', пішохід' if self.auto == [] else f', авто: {", ".join(auto_str)}'
        return f'{self.name} {self.surname}{is_auto}'


car_1 = Car('BMW-5', 'AE 234-23')
car_2 = Car('LADA-2103', 'AE 111-56')

# print(car_1.model)
# print(car_1.number)
print(car_1)

user = User('Іван', 'Іванов', [car_1, car_2])
print(user)
