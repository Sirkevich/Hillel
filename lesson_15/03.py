people = [
    {'name': 'Jack', 'phone': 1234235},
    {'name': 'Rick', 'family': True, 'children': None},
    {'name': 'Bob', 'children': (('Kati', 12), ('Nick', 7))},
    {'name': 'Tim', 'job': 'engenere'},
    {'name': 'Lussy', 'pets': ['Rem', 'Sam']}
]


class People:
    def __init__(self, name, phone=None, family=None, children=None, job=None, pets=None):
        self.name = name
        self.phone = phone
        self.family = family
        self.children = children
        self.job = job
        self.pets = pets


a_1 = People(people[0].get('name'), phone=people[0].get('phone'))
a_2 = People(people[1].get('name'), family=people[1].get('family'), children=people[1].get('children'))
a_3 = People(people[2].get('name'), children=people[2].get('children'))
a_4 = People(people[3].get('name'), job=people[3].get('job'))
print(a_1.__dict__)
print(a_2.__dict__)
print(a_3.__dict__)
print(a_4.__dict__)
