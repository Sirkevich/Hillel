name = 'Tom'


def say_hi(name_global):

    print(f'Hi, {name_global}')
    name = 'Bob'
    print(f'Bye, {name}')


say_hi(name)
