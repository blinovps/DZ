class MyDate:
    """Формат даты "dd.mm.yyyy"
    с 1920 по 2020 годы"""

    def __init__(self, dd_mm_yyyy):
        self.date = dd_mm_yyyy

    @classmethod
    def ext(cls, dd_mm_yyyy):
        date = []
        for el in str(dd_mm_yyyy).split("."):
            date.append(el)
        return f"{int(date[0])}.{int(date[1])}.{int(date[2])}"

    @staticmethod
    def check(dd_mm_yyy):
        x = dd_mm_yyy
        date = []
        for el in str(x).split("."):
            date.append(el)
        dd = int(date[0])
        mm = int(date[1])
        yyyy = int(date[2])
        if 1 <= dd <= 31 and 1 <= mm <= 12 and 1920 <= yyyy <= 2020:
            return f"{dd}.{mm}.{yyyy} - Дата введена верно."
        else:
            return f"{dd}.{mm}.{yyyy} - Дата введена неверно."


d1 = MyDate("11.11.1111")
print(d1.date)
print(MyDate.ext("1.2.123"))
print(MyDate.check("11.12.2000"))
print(MyDate.check("33.12.2000"))
print(MyDate.check("11.13.2000"))
print(MyDate.check("11.12.2200"))
