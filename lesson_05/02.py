a = 'AAA'
b = 'TTY'

print(a + b)
print(b + a)
print(b * 5)
print(a + ' ' + b * 5 + ' ' + a * 2 + ' ' + b)


a = "I'd like ..."
b = 'DFEg "dfgdg" and "TTFDGH" lknkl.'
b2 = 'DFEg "dfgdg" and "TTFDGH" \nlknkl.'
b_1 = r'DFEg "dfgdg" \t and \n "TTFDGH" lknkl.'
c_1 = """I'd like ...DFEg "dfgdg" and "TTFDGH" lknkl."""
c_2 = "I'd like ...DFEg \"dfgdg\" and \"TTFDGH\" lknkl."

print(a)
print(b)
print(c_1)
print(c_2)
print(b_1)

print(len(b))
print(len(b2))
print("TTFDd" in b)

print(b[4:-2:2])
