# виведе на екран прямокутник із символів «*».
a = int(input("Input a "))
b = int(input("Input b "))
i = 0
while i < a:  # Висота
    j = 0
    while j < b:  # ширина
        print("*", end='')  # рядок не буде переведено
        j += 1
    print()
    i += 1
