class Warehouse:
    warehouse = {}
    company_division = {}
    name = 1  # Инвентарный №

    def __init__(self, in_stoke):
        self.in_stoke = in_stoke
        self.name = Warehouse.name
        Warehouse.name += 1

    def get_in(self):
        """Добавление на склад"""
        d = {self.name: self}
        Warehouse.warehouse.update(d)
        self.in_stoke = True
        try:
            Warehouse.company_division.pop(self.name)
        except KeyError:
            return ""

    def get_out(self):
        """Передача в подразделение 'company_division' """
        d = {self.name: self}
        Warehouse.company_division.update(d)
        Warehouse.warehouse.pop(self.name)
        self.in_stoke = False


class Tech(Warehouse):
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        super().__init__(in_stoke=None)


class Printer(Tech):
    def __init__(self, brand, model, price, printer_type, color=False):
        self.printer_type = printer_type  # matrix, jet, laser.
        self.color = color  # color, b/w
        super().__init__(brand, model, price)

    def __repr__(self):
        return f"{self.name} - Принтер {self.in_stoke}"


class Scanner(Tech):
    def __init__(self, brand, model, price, size):
        self.size = size  # A3, A4 etc
        super().__init__(brand, model, price)

    def __repr__(self):
        return f"{self.name} - Сканер {self.in_stoke}"


class Copier(Tech):
    def __init__(self, brand, model, price, speed):
        self.speed = speed  # copies/minute
        super().__init__(brand, model, price)

    def __repr__(self):
        return f"{self.name} - Копир {self.in_stoke}"


while True:
    printer_attr = ["brand", "model", "price", "printer_type"]
    scanner_attrib = ["brand", "model", "price", "size"]
    copier_attrib = ["brand", "model", "price", "speed"]

    tech_type = {1: "Printer", 2: "Scanner", 3: "Copier"}
    t_t_num = input(f"Введите тип оргтехники:\n 1 - Printer\n 2 - Scanner\n 3 - Copier\n(Enter для выхода):")
    if t_t_num == "":
        break







"""
pr1 = Printer("qq", "ww", 33, "jet")
cp1 = Copier("aa", 123, 345, 100)
scan1 = Scanner("zzz", "qwe123", 123, "A3")
cp1.get_in()
scan1.get_in()
pr1.get_in()
print(Warehouse.warehouse)
print(Warehouse.company_division)
scan1.get_out()
print(Warehouse.warehouse)
print(Warehouse.company_division)
scan1.get_in()
print(Warehouse.warehouse)
print(Warehouse.company_division)
"""