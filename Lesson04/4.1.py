from sys import argv

script_name, time, rate, bonus = argv


def my_func(time, rate, bonus):
    wage = (float(time) * float(rate)) + float(bonus)
    return wage


print(f"Зарплата:{my_func(time, rate, bonus):.2f}")
