start = int(input("Введите начальный результат:"))
finish = int(input("Введите конечный результат:"))
day = 1
while finish > start:
    start += start * 0.1
    day += 1
print(f"Результат будет достигнут на {day} день")