class Auto:
    numbers = 0

    def __init__(self, color='White', model='BMV-7'):
        self.color = color
        self.model = model
        self.incriment_number()

    @classmethod
    def incriment_number(cls):
        cls.numbers += 1


a_1 = Auto()
a_2 = Auto()
a_3 = Auto()
print(Auto.numbers)


class Truck(Auto):
    numbers = 0


b_1 = Truck()
b_2 = Truck()
print(Truck.numbers)
print(Auto.numbers)
