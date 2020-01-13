my_dict = {"Зима": (12, 1, 2), "Весна": (3, 4, 5), "Лето": (6, 7, 8), "Осень": (9, 10, 11)}
num = int(input("Введите число месяца:"))
for season in my_dict.keys():
    for month in my_dict.get(season):
        if month == num:
            print(season)