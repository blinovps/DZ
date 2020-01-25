import re

with open("5.6.txt", "r", encoding="utf-8") as f:
    my_dict = {}
    for line in f.readlines():
        v = 0
        k = re.findall(r"^\w+\b", line)
        num = re.findall(r"\b\d+", line)
        for el in num:
            v += int(el)
        d = {str(k)[2:-2]: v}
        my_dict.update(d)
print(my_dict)
