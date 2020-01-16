def my_func(a, b, c):
    l = [a, b, c]
    l.remove(min(l))
    return l[0] + l[1]


print(my_func(3, 4, 1))