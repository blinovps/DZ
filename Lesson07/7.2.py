from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def material(self):
        pass


class Coat:
    def __init__(self, x):
        self.size = x

    @property
    def material(self):
        return f"Расход ткани на пальто(Размер:{self.size}) = {self.size / 6.5 + 0.5:.3f}"


class Costume:
    def __init__(self, x):
        self.height = x

    def material(self):
        print(f"Расход ткани на костюм(Рост:{self.height}) = {(2 * self.height + 0.3):.3f}")


coat1 = Coat(10)
print(coat1.material)

costume1 = Costume(10)
costume1.material()
