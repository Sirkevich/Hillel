print('START')
try:
    a = [10, 56, 24]
    b = 67
    c = a[5] / b
except ZeroDivisionError:
    c = 1
    e = 0
except (TypeError, NameError):
    c = 100
except Exception as err:
    print(err)
    c = -100
else:
    print('ELSE')
finally:
    print('FINALLY')

d = 1000
print(d - c)

print('FINISH')
