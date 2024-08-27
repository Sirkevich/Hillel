class Car(object):
    wheels = 4  # атрибут класу
    color = 'Red'
    model = None

    def __init__(self, *args):
        self.color = args[0] if len(args) > 0 else None
        self.model = args[1] if len(args) > 1 else None

    def start_engine(self):
        return "Engine started!"

    def test_car(self):
        print('Test copmleted')


car_1 = Car('Black', 'BMW')
car_2 = Car('ZAZ', 'Yellow')
car_3 = Car('Opel')

print(f'attributes of car 1: {car_1.__dict__}')
print(f'attributes of car 2: {car_2.__dict__}')
print(f'attributes of car 3: {car_3.__dict__}')
