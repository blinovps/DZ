import json
with open("5.7.txt", "r", encoding="utf-8") as f:
    q = 0
    p = 0
    firm_list = {}
    average_profit = 0
    for line in f.readlines():
        line = str(line).split()
        profit = int(line[2]) - int(line[3])
        if profit > 0:
            q += 1
            p += profit
        d = {line[0]: profit}
        firm_list.update(d)
    average_profit = p / q
with open("5.7.json", "w", encoding="utf-8") as f:
    json.dump([firm_list, {"average_profit": average_profit}], f, indent=4)
