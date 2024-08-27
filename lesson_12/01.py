class Car:
    wheels = 4  # атрибут класу
    color = 'Red'

    def start_engine(self):
        return "Engine started!"

    def test_car(self):
        print('Test copmleted')


car_1 = Car()
car_2 = Car()
car_3 = Car()

car_2.wheels = 5

print(f'wheels of car 1: {car_1.wheels}')
print(f'wheels of car 2: {car_2.wheels}')
print(f'wheels of car 3: {car_3.wheels}')

car_2.test_car()
print(car_2.test_car)

print(f'attributes of car 1: {car_1.__dict__}')
print(f'attributes of car 2: {car_2.__dict__}')
print(f'attributes of car 3: {car_3.__dict__}')

Car.wheels = 3
print(f'wheels of car 1: {car_1.wheels}')
print(f'wheels of car 2: {car_2.wheels}')
print(f'wheels of car 3: {car_3.wheels}')

car_1.name = 'BMW'
car_1.year = 2023

print(car_1.year)
# print(car_2.year)
