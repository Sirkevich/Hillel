b = 'helLo, WolRld!'
b_1 = '    helLo, WolRld!     '
b_2 = '!helLo, !Wol!Rld!!'
b_3 = '!helLo,    !Wol!Rld!WO! RedWo       FT!Wo'

print(b.replace('W', 'g'))
print(b.replace('l', '!'))
print(b.replace('l', 'c', 2))

print(b_1.strip())
print(b.strip('!'))
print(b_2.strip('!'))
print(b_2.strip('ld!h'))

print(b_2.split())
print(b_3.split())
print(b_3.split('R'))
print(b_3.split('Wo'))

d = b_3.split('Wo')

for index, word in enumerate(d):
    d[index] = word.strip('! ')

print(d)
