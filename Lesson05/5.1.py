str_list = []
x = True
while x == True:
    my_str = str(input("Введите строку(для выхода нажмите Enter):"))
    if my_str == "":
        x = False
        break
    str_list.append(f"{my_str}\n")
with open("5.1.txt", 'w', encoding='utf-8') as f:
    f.writelines(str_list)