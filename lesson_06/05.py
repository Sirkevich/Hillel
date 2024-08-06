a = {"red": "червоний", "black": "чорний", "yellow": "жовтий"}

print(a.setdefault("red", "не визначено"))
print(a.get("pink", "не визначено"))
print(a)

print(a.setdefault("pink", "не визначено"))
print(a)
