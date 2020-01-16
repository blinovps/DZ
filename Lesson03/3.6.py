def int_func(word):
    return word.title()


#print(int_func("qwe"))
my_list = list(input("Введите слова через пробел:").split())
for el in my_list:
    int_func(el)
    print(int_func(el), end=" ")
