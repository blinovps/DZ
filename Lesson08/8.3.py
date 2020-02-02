import re


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


data = []
while True:
    num = input("Введите число(Enter для выхода):")
    if num == "":
        print(data)
        break
    try:
        x = re.findall(r"[ ]*[-+]?\d*\.?\d*[ ]*", num)
        #print(x)
        if x == re.findall(r"[ ]*", num) or str(num) != x[0]:
            raise OwnError("Введено не число.")
    except OwnError as err:
        print(err)
    else:
        data.append(re.findall(r"[-+]?\d+\.?\d*", x[0]))
