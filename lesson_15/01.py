class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color ={}]"
        return msg.format(self.name, self.age, self.color)

    # def __getattr__(self, atr_name):
    #     return f"Attribute '{atr_name}' is absent"


cat = Cat('Barsik', 3, 'black')
print(cat.name)
# print(cat.type)

print(getattr(cat, "name", 111))
print(getattr(cat, "age"))
print(getattr(cat, "color", 111))
print(getattr(cat, "type", 111))

del cat.age
# print(getattr(cat, "age"))

print(hasattr(cat, "name"))  # виведе True
print(hasattr(cat, "age"))  # виведе True
print(hasattr(cat, "color"))  # виведе True
print(hasattr(cat, "gender"))  # виведе False

print(cat.__dict__)
