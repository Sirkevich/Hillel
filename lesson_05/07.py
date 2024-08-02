template = 'My name is {}. I am {} years old. {} is cool name'
template_2 = 'My name is {0}. I am {2} years old. {0} is cool name'
template_3 = 'My name is {name:^10}. I am {age:3} years old. {name:<10} is cool name'

template_4 = 'Object has {:.2%}'

name = 'Bob'
age = 32

a_1 = 12
a_2 = 35

print(template.format(name, age, name, 'Kate'))
print(template_2.format(name, age, name + '!', 'Kate'))
print('-' * 100)
print(template_3.format(name='Bob', age=age))
print(template_3.format(name='Evgeniy', age=1))
print(template_3.format(name='Kate', age=102))
print('-' * 100)
print(template_4.format(a_1 / a_2))
