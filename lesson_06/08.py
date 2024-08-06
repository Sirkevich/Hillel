from collections import namedtuple

Airplane = namedtuple('Airplane', 'sits year number name')

air_1 = (450, 1989, "DR-4435", "Boing-777")
air_2 = (320, 2003, "AE-0098", "Boing-777")
air_3 = (120, 2010, "ZE-RRTE", "Sesna")

print(f"Number of sits: {air_1[0]}")
print(f"Number of airplane: {air_3[2]}")

air_01 = Airplane(450, 1989, "DR-4435", "Boing-777")
air_02 = Airplane(320, 2003, "AE-0098", "Boing-777")
air_03 = Airplane(120, 2010, "ZE-RRTE", "Sesna")

print(f"Number of sits: {air_01.sits}")
print(f"Number of airplane: {air_03.number}")
print(f"Number of airplane: {air_03[2]}")

airs = [air_01, air_02, air_03]

print(type(air_01))
print(type(air_1))
