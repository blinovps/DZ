with open("5.2.txt", 'r', encoding='utf-8') as f:
    x = 0
    for line in f:
        x += 1
        print(f"Количество слов в строке {x} - {len(line.split())}")
print(f"Всего {x} строк")