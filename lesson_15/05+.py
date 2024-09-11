class MyString(str):
    def __iter__(self):
        self.start = -1
        self.data = self.split()
        return self

    def __next__(self):
        while self.start < len(self.data) - 1:
            self.start += 1
            return self.data[self.start].replace(',', '').replace('.', '').title()
        raise StopIteration


a = MyString('Hello, world. SECOND sence.')

print(a)

for item in a:
    print(item)
