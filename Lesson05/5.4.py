with open("5.4.txt", 'r', encoding='utf-8') as f:
    my_list = []
    text = f.read()
    text = text.replace("One", "Один")
    text = text.replace("Two", "Два")
    text = text.replace("Three", "Три")
    text = text.replace("Four", "Четыре")
with open("5.4.a.txt", "w", encoding="utf-8") as f:
    f.writelines(text)
