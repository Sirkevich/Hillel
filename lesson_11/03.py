file = open('file_2.txt')
try:
    text = file.read(14)
    text_2 = file.read(5)
finally:
    file.close()

print(text)
print(text_2)
