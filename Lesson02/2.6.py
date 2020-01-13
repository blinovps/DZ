num = 1
my_list = []
sort = {"название": list(), "цена": list(), "количество": list(), "еденица измерения": list()}
x = "yes"
while x == "yes":
    my_dict = {"название": input("Введите название:"), "цена": input("Введите цену:"),
               "количество": input("Введите количество:"), "еденица измерения": input("Введите еденицу измерения:")}
    my_list.append((num, my_dict))
    for key in my_dict.keys():
        sort[key].append(my_dict.get(key))
    x = input("Хотите продолжить ввод? yes/no:")
    num += 1
for a in my_list:
    print(a)
for a in sort.keys():
    print(a, ":", sort.get(a))