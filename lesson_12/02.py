class Car:
    wheels = 4  # атрибут класу
    color = 'Red'
    name = None

    def start_engine(self):
        return "Engine started!"

    def test_car(self):
        print(f'Test copmleted for: {self.name}')
        # print(self.start_engine())


car_1 = Car()
car_1.color = 'Black'
car_1.name = 'BMW'

car_2 = Car()
car_2.color = 'Yellow'
car_2.name = 'ZAZ'

car_3 = Car()
# car_3.color = 'Red'
car_3.name = 'OPEL'

print(car_3.color)

Car.color = "BLUE"
print(car_3.color)

car_1.test_car()
car_2.test_car()
