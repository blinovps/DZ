class Road:
    def __init__(self, lenght, width):
        self._mass1 = 25
        self._thickness = 5
        self._lenght = lenght
        self._width = width

    def mass_all(self):
        print(f"Масса асфальта: {(self._lenght * self._width * self._mass1 * self._thickness) / 1000} тонн")


asphalt = Road(50000, 40)
asphalt.mass_all()
