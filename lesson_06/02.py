t = (1, "hello", [3, 4, 5])
a = [1, "hello", [3, 4, 5]]

print(t)
print(type(t))
print(a)
print(type(a))

print(t.count("hello"))
print(a.count("hello"))

print(t[1])
n = t[:2]
print(n)
print(type(n))

t[2].append(0)
print(t)
