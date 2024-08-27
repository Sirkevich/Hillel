class Animal:
    number_of_foot = 4
    is_tail = True

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'step{item} ', end='')
        print()

    def say(self):
        print('Nothing')


# class Dog:
class Dog(Animal):
    def say(self):
        print('Wof-Wof-Wof!')


class Cat(Animal):
    def say(self):
        print('Miau')


a_1 = Dog()
a_1.number_of_foot = 3
a_1.go()
a_1.say()

print('-' * 100)

a_2 = Cat()
a_2.go()
a_2.say()
