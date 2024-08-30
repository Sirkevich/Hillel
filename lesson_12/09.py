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

    def traner(self):
        print('TRANER')


class Cat(Animal):
    def say(self):
        print('Miau')
        super().say()

    def catch_fish(self):
        return '111'


class Monster(Dog, Cat):
    def say(self):
        print('3444')
        super().say()
        print('I am a moster')


monster_1 = Monster()
monster_1.go()
print(monster_1.catch_fish())
monster_1.traner()
monster_1.say()

cat_1 = Cat()
cat_1.say()
