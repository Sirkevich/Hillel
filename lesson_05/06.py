template = 'My name is %s. I am %s years old. %s is cool name'
template_2 = 'My name is %(name)s. I am %(age)s years old. %(name)s is cool name'

name = 'Bob'
age = 32

print(template % (name, age, name))
print(template_2 % {'name': name + '!', 'age': 34})
