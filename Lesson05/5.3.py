with open("5.3.txt", 'r', encoding='utf-8') as f:
    less_20 = []
    average = 0
    x = 0
    for line in f.readlines():
        if int(list(line.split())[1]) < 20000:
            less_20.append(list(line.split())[0])
        average += int(list(line.split())[1])
        x += 1
print(f"Оклад меньше 20000 - {less_20}")
print(f"Средний оклад - {average / x:.2f}")