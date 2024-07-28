number = 0
c = None

print('START')

if number > 10:
    print('more than 10')
elif number > 5:
    print('more than 5')
    if number < 0:
        print('less than 0')
    elif number == 0:
        print('number == 0')
elif number > 0:
    print('more than 0')
    c = 0
    c += 5
elif number < -5:
    print('less than -5')
else:
    print('ELSE')
    c = 0

print('c =', c)
print('END')
