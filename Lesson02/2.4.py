my_list = list(input("Введите слова через пробел:").split())
n = 0
for x in my_list:
    n += 1
    print(f"{n} - {x[:10]}")