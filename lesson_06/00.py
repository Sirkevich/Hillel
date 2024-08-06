import random

print( "LIST START" )
a = random.randint(1, 100)
b = [random.randint(3, 10) for b in range(a)]
print(b)
c = b.pop(0)
d = b.pop(1)
e = b.pop(-2)
f = [c, d, e]
print(f)
print( "LIST END" )



import random

print("LIST START")
input_list = [random.randint(3, 10) for b in range(random.randint(1, 100))]
print(input_list)
result_list = [input_list.pop(0), input_list.pop(1), input_list.pop(-2)]
print(result_list)
print("LIST END")
