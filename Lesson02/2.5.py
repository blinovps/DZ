my_list = [6]
num = 0
while num != "q":
    num = input("Введите число(Для выхода введите q):")
    if num == "q":
        break
    l = my_list.copy()
    for el in l:
        x = l.index(el)
        if int(num) > int(el):
            my_list[x:x] = [num]
            print(my_list)
            break
        elif int(el) < int(num):
            my_list[x:x] = [num]
            print(my_list)
            break
        elif el == l[-1]:
            my_list.append(num)
            print(my_list)



