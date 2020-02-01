class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return self.quantity - other.quantity
        else:
            return "Вычитание невозможно"

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return round(self.quantity / other.quantity)

    def make_order(self, cells):
        #row = f"{cells * '*'}\n"
        rows = self.quantity // cells
        last_row = self.quantity % cells
        print(f"{cells * '*'}\n" * rows + f"{last_row * '*'}\n")


cell1 = Cell(10)
cell2 = Cell(15)
cell3 = Cell(20)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell3 / cell1)
print(cell3 / cell2)
cell1.make_order(4)
