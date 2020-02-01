class Matrix:
    def __init__(self, list1):
        self.list1 = list1

    def __add__(self, other):
        self.matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] = self.list1[x][y] + other.list1[x][y]
        return str('\n' .join(['\t' .join([str(x) for x in y]) for y in self.matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(x) for x in y]) for y in self.list1]))


mat1 = Matrix([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
#print(mat1)
mat2 = Matrix([[11, 21, 31], [12, 22, 32], [13, 23, 33]])
print(mat1 + mat2)

