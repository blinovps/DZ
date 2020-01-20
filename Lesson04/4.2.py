import random
my_list = []
list_1 = random.sample(range(20), 20)
x = list_1[0]
for el in list_1[1:]:
    if el > x:
        my_list.append(el)
    x = el
print(list_1)
print(my_list)