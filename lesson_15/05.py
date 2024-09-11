class MyIter:
    def __init__(self, data):
        self.data = data.split()
        self.start = -1

    def __next__(self):
        while self.start < len(self.data) - 1:
            self.start += 1
            return self.data[self.start].replace(',', '').replace('.', '').title()
        raise StopIteration


class MyString(str):
    def __iter__(self):
        return MyIter(self)


a = MyString('Hello, world. SECOND sence.')

print(a)

for item in a:
    print(item)
