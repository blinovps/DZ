class ComplexNum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        if num2 < 0:
            self.x = f"{num1}{num2}j"
        else:
            self.x = f"{num1}+{num2}j"

    def __add__(self, other):
        if int(self.num2) + int(other.num2) < 0:
            return f"{int(self.num1) + int(other.num1)}{int(self.num2) + int(other.num2)}j"
        else:
            return f"{int(self.num1) + int(other.num1)}+{int(self.num2) + int(other.num2)}j"

    def __mul__(self, other):
        if int(self.num2) * int(other.num1) - int(self.num1) * int(other.num2) < 0:
            return f"{int(self.num1) * int(other.num1) - int(self.num2) * int(other.num2)}" \
                   f"{int(self.num2) * int(other.num1) - int(self.num1) * int(other.num2)}j"
        else:
            return f"{int(self.num1) * int(other.num1) - int(self.num2) * int(other.num2)}+" \
                   f"{int(self.num2) * int(other.num1) - int(self.num1) * int(other.num2)}j"


cm1 = ComplexNum(3, -5)
cm2 = ComplexNum(-6, 3)
print(cm1.x)
print(cm2.x)
print(cm1 + cm2)
print(cm1 * cm2)
