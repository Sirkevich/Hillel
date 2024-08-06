a = {"red": "червоний", "black": "чорний", "yellow": "жовтий"}
b = {1: "erer", 2: 20, (1, 3, 0): [1, 2, "df"], 4: {1: 0, 2: 1}, "new": 20}

print(len(a))
print(a["yellow"])
print(a.get("pink"))
print(a.get("yellow"))

print('-' * 100)
print(a.get("red", "не визначено"))
print(a.get("pink", "не визначено"))

print(len(b))
print(b[4])
print(b[2])
print(b["new"])
b["new"] = 777
print(b["new"])
b["new_2"] = 100
print(b)
b.update({"rr": 99, "ww": 0, 1: 88})
print(b)

c = b.pop(4)
print(b)
print(c)

print(b.values())
print(b.keys())

for key in b.keys():
    print(key)

print('-' * 100)
for item in b.items():
    print(item)

for key, value in b.items():
    print(f"{key} - {value}")
