import random
list_1 = random.sample(range(15), 10) + random.sample(range(15), 10)
my_list = [el for el in list_1 if list_1.count(el) == 1]
print(list_1)
print(my_list)