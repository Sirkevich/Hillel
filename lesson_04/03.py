a = 10

while a < 0:
    if a % 3 == 0:
        a -= 1
        continue
    if a < 3:
        break
    print(a)
    a -= 1
else:
    print('End of WHILE')


print('END')


while True:
    ...
