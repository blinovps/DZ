class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


data1 = input("Введите делимое:")
data2 = input("Введите делитель:")

try:
    int(data1)
    int(data2)
    if int(data2) == 0:
        raise OwnError("На ноль делить нельзя")
except ValueError:
    print("Введено не число.")
except OwnError as err:
    print(err)
else:
    print(f"Результат {int(data1) / int(data2):.02f}")
