def div(num1, num2):
    try:
        num1 / num2
    except ZeroDivisionError:
        return "Нельзя делить на ноль"
    return num1 / num2


print(div(int(input("Введите делимое:")), int(input("Введите делитель:"))))