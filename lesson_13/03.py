class MyExcept(Exception):
    pass


print('START')

try:
    a = [10, 56, 24]
    b = 0
    if b == 0:
        raise MyExcept
    c = a[2] / b
except MyExcept:
    print('EXCEPT')

print('FINISH')
