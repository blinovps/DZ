class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановиась")

    def turn(self, direction):
        self.direction = direction
        if self.direction == "right":
            print(f"Машина {self.name} повернула направо")
        elif self.direction == "left":
            print(f"Машина {self.name} повернула налево")
        else:
            print(f"direction = 'left' or 'right'")

    def show_speed(self):
        print(f"Скорость машины {self.name} - {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости. Скорость машины {self.name} - {self.speed}")
        else:
            print(f"Скорость машины {self.name} - {self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости. Скорость машины {self.name} - {self.speed}")
        else:
            print(f"Скорость машины {self.name} - {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed,  name, color="white-blue", is_police=True):
        super().__init__(speed, color, name, is_police)


car1 = Car(50, "red", "Name1")
car1.go()
car1.stop()
car1.turn("left")
car1.turn("right")
car1.turn("back")
car1.show_speed()

town_car1 = TownCar(50, "red", "Town1")
town_car1.show_speed()

town_car2 = TownCar(100, "blue", "Town2")
town_car2.show_speed()

work_car1 = WorkCar(30, "black", "Work1")
work_car1.show_speed()

work_car2 = WorkCar(100, "green", "Work2")
work_car2.show_speed()
