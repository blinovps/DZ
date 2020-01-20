from math import factorial


def func(a):
    b = a + 15
    while a != b:
        yield factorial(a)
        a += 1


for x in func(15):
    print(x)
