dohod = int(input("Введите выручку:"))
rashod = int(input("Введите издежки:"))
if dohod > rashod:
    itog = dohod - rashod
    shtat = int(input("Введите количество сотрудников:"))
    print(f"Прибыль фирмы - {itog} \n"
          f"Рентабельность - {itog / dohod} \n"
          f"Прибыль на одного сотрудника - {dohod / shtat}")
else:
    print(f"Убыток фирмы -", rashod - dohod)
    