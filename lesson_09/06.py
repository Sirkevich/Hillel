a = ['rt', 'r', '', '445d', 'ee']


def func_1(x: str) -> str:
    return x + str(len(x))


res_1 = map(func_1, a)
# print(res_1)
# for item in res_1:
#     print(item)

print(list(res_1))

res_2 = map(lambda x: x + str(len(x)), a)
print(list(res_2))


def func_2(x: str) -> bool:
    return len(x) > 2


res_3 = filter(func_2, a)
print(list(res_3))

res_4 = filter(lambda x: len(x) > 2, a)
print(list(res_4))

