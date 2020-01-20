import itertools


def func_a(*args):
    """Целые числа с шагом +1
     Первый аргумент - начальное число
     Второй аргумент конечное число"""
    for el in itertools.count(args[0]):
        if el > args[1]:
            break
        yield el


def func_b(*args):
    """Цикличный вывод значений из списка
    Первый аргумент - список
    Второй аргумент - количество значений"""
    a = 1
    for x in itertools.cycle(args[0]):
        if a > args[1]:
            break
        a += 1
        yield x


for el in func_a(10, 20):
    print(el)
for x in func_b([1, 3, "q", "w"], 6):
    print(x)
