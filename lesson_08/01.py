name = 'Tom'


def say_hi():
    def say():
        global name
        name = 'Kite'
        print(name.upper())

    name = 'Bob'
    print(f'Hi, {name}')
    say()


def say_bye():
    name = 'Sara'
    print(f'Bye, {name}')
    return name


say_hi()
name = say_bye()
# say()
print(name)
