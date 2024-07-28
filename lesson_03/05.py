number = True

if number is True:
    a = 10
else:
    a = 20

a = 10 if number is True else 20



if number is True:
    a = 10
else:
    if number is None:
        a = 20
    else:
        a = 0

a = 10 if number is True else 20 if number is None else 0
