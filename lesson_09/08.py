def my_func(a=90):
    ...
    yield a + 10
    a += 1
    yield a
    a += 1
    yield a
    print('finish')


count = 3
for item in my_func():
    if count <= 0:
        break
    print(item)
    count -= 1

# fibonacci = my_func()
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
