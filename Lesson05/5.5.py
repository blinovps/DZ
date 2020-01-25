import random
with open("5.5.txt", "w", encoding="utf-8") as f:
    for el in random.sample(range(50), 20):
        f.writelines(f"{str(el)} ")
with open("5.5.txt", "r", encoding="utf-8") as f:
    x = 0
    for el in str(f.read()).split():
        x += int(el)
    print(f"Сумма чисел - {x}")