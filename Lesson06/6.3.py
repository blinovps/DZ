class Worker:
    def __init__(self, name, surname, position="default position", wage=100, bonus=50):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position="Position1", wage=200, bonus=100):
        super().__init__(name, surname, position, wage, bonus)

    def __repr__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Poition: {self.position}, Income: {self.income}"

    def get_full_name(self):
        print(f"Полное имя: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Доход: {self.income.get('wage') + self.income.get('bonus')}")


subj = Position("Name1", "Surname1")
#print(subj)
subj.get_full_name()
subj.get_total_income()

