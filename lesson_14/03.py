class String(str):
    def __sub__(self, other):
        res = self
        for symbol in other:
            if symbol in res:
                res = res.replace(symbol, '', 1)
        return res


a = String('ruiti')
b = String('uui')

print(a.upper())

print((a + b).capitalize())
print(a - b)
