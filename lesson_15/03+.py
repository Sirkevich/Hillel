people = [
    {'name': 'Jack', 'phone': 1234235},
    {'name': 'Rick', 'family': True, 'children': None},
    {'name': 'Bob', 'children': (('Kati', 12), ('Nick', 7))},
    {'name': 'Tim', 'job': 'engenere'},
    {'name': 'Lussy', 'pets': ['Rem', 'Sam'], 'depth': True}
]


class People:
    pass


a_1 = People()
a_2 = People()
a_3 = People()
a_4 = People()
a_5 = People()

a = [a_1, a_2, a_3, a_4, a_5]
for index, item in enumerate(people):
    for key, val in item.items():
        setattr(a[index], key, val)

print(a_1.__dict__)
print(a_2.__dict__)
print(a_3.__dict__)
print(a_4.__dict__)
print(a_5.__dict__)
