class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color ={}]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        if atr_name == "type":
                return "Home Cat"
        print(atr_name)
        return "11"

    def __getattribute__(self, atr_name):
        return object.__getattribute__(self, atr_name)

    def __setattr__(self, attr_name, attr_value):
        if attr_name == 'age':
            if isinstance(attr_value, int) and 0 <= attr_value <= 20:
                self.__dict__[attr_name] = attr_value
        else:
            self.__dict__[attr_name] = attr_value


cat = Cat('Barsik', 3, 'black')

cat.type = "Devil"
print(cat.type)

print(cat.__dict__)

cat.age = 12
print(cat.age)
cat.age = 22
print(cat.age)
cat.age = 1.23
print(cat.age)
