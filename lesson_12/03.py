class Car:
    wheels = 4  # атрибут класу
    color = 'Red'
    model = None

    def __init__(self, model, color='Red'):
        self.color = color
        self.model = model

    def start_engine(self):
        return "Engine started!"

    def test_car(self):
        print('Test copmleted')


car_1 = Car(color='Black', model='BMW')
car_2 = Car('ZAZ', 'Yellow')
car_3 = Car('Opel')

print(f'attributes of car 1: {car_1.__dict__}')
print(f'attributes of car 2: {car_2.__dict__}')
print(f'attributes of car 3: {car_3.__dict__}')
