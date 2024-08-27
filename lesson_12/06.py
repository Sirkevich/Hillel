class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y


a_1 = MathOperations()
print(a_1.add(3, 5))
print(MathOperations.add(3, 5))

# result = MathOperations.add(3, 5)
# print(result)
