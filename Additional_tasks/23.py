# Напишіть програму, яка приймає список чисел і повертає суму, мінімальне та 
# максимальне значення зі списку. Використовуйте функцію для обробки списку 
# чисел та повернення трьох значень. Виведіть результат на eкран за допомогою 
# команди print.
#
# Приклад:
# Введіть числа через кому та пробіл: 3, 7, 2, 9, 1, 5
# Сума чисел: 27
# Мінімальне значення: 1
# Максимальне значення: 9


def vse(a):
    for i in range(len(a)):
        a[i] = int(a[i])
    return sum(a), max(a), min(a)


x = input("Введіть числа: ").split(', ')
s, mx, mn = vse(x)
print("Сума чисел:", s)
print("Мінімальне значення:", mx)
print("Максимальне значення:", mn)
