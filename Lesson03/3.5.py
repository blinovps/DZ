def my_sum(*args):
    s = 0
    x = "yes"
    while x == "yes":
        num = input("Введите числа(q для выхода):").split()
        for el in num:
            if el == "q":
                x = "no"
                break
            else:
                s += int(el)
        print(s)
    return s


print(my_sum())
