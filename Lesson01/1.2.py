s = int(input("Введите количество секунд:"))
hour = s // 3600
minute = (s - (hour * 3600)) // 60
second = (s - (hour * 3600)) % 60
print(f"{hour:02.0f}:{minute:02.0f}:{second:02.0f}")
