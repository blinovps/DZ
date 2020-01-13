my_list = list(input("Введите элементы списка через пробел:").split())
lenght = len(my_list)
el = 0
while el < lenght - 1:
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)