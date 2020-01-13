my_list = ["Зима", "Весна", "Лето", "Осень"]
num = int(input("Введите число месяца:"))
if num == 1 or num == 2 or num == 12:
    print(my_list[0])
elif 2 < num < 6:
    print(my_list[1])
elif 5 < num < 8:
    print(my_list[2])
else:
    print(my_list[3])