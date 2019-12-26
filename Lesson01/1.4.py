num = int(input("Введите число:"))
max = -1
while num > 0:
    i = num % 10
    num //= 10
    if i > max:
        max = i
print("Самая большая цифра в числе:", max)