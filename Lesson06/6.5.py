class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title}. Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title="Ручка"):
        super().__init__(title)


class Pencil(Stationery):
    def __init__(self, title="Крандаш"):
        super().__init__(title)


class Handle(Stationery):
    def __init__(self, title="Маркер"):
        super().__init__(title)


pen1 = Pen()
pen1.draw()

pencil1 = Pencil()
pencil1.draw()

handle1 = Handle()
handle1.draw()
