class Matrix:
    def __init__(self, lines, columns):
        self.row = lines
        self.col = columns
        self.matrix = [[0 for _ in range(columns)] for _ in range(lines)]

    def allocate(self):
        if self.row != 0 and self.col != 0:
            self.matrix = [[0 for _ in range(self.col)] for _ in range(self.row)]

    def deallocate(self):
        self.matrix = []

    def initialize(self):
        self.matrix = [[0 for _ in range(self.col)] for _ in range(self.row)]

    def set_size(self, lines, columns):
        self.deallocate()
        self.row = lines
        self.col = columns
        self.allocate()
        self.initialize()

    def get(self, i, j):
        return self.matrix[i][j]

    def set(self, i, j, value):
        self.matrix[i][j] = value

    def copy_from(self, other):
        assert self.row == other.row and self.col == other.col
        self.matrix = [row[:] for row in other.matrix]

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))
        print("--------")

    def identity(size):
        return Matrix.diag(size, 1)

    def diag(size, diag_value):
        M = Matrix(size, size)
        for i in range(size):
            M.set(i, i, diag_value)
        return M

    def tran(self):
        N = Matrix(self.col, self.row)
        for i in range(self.row):
            for e in range(self.col):
                N.set(e, i, self.matrix[i][e])
        return N

    def inv(self):
        N = Matrix(self.col, self.row)
        if self.row == 1 and self.col == 1:
            N.set(0, 0, 1 / self.get(0, 0))
        elif self.row == 2 and self.col == 2:
            det = self.get(0, 0) * self.get(1, 1) - self.get(1, 0) * self.get(0, 1)
            N.set(0, 0, self.get(0, 0) / det)
            N.set(0, 1, -self.get(0, 1) / det)
            N.set(1, 1, self.get(1, 1) / det)
            N.set(1, 0, -self.get(1, 0) / det)
        return N

    def __add__(self, other):
        assert self.row == other.row and self.col == other.col
        temp = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                temp.set(i, j, self.matrix[i][j] + other.get(i, j))
        return temp

    def __sub__(self, other):
        assert self.row == other.row and self.col == other.col
        temp = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                temp.set(i, j, self.matrix[i][j] - other.get(i, j))
        return temp

    def __radd__(self, k):
        temp = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                temp.set(i, j, self.matrix[i][j] + k)
        return temp

    def __rsub__(self, k):
        temp = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                temp.set(i, j, k - self.matrix[i][j])
        return temp

    def __mul__(self, other):
        if isinstance(other, Matrix):
            assert self.col == other.row
            temp = Matrix(self.row, other.col)
            for i in range(self.row):
                for j in range(other.col):
                    temp.set(i, j, sum(self.matrix[i][k] * other.get(k, j) for k in range(self.col)))
            return temp
        else:
            temp = Matrix(self.row, self.col)
            for i in range(self.row):
                for j in range(self.col):
                    temp.set(i, j, self.matrix[i][j] * other)
            return temp

    def __rmul__(self, k):
        temp = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                temp.set(i, j, self.matrix[i][j] * k)
        return temp

    def __iadd__(self, other):
        assert self.row == other.row and self.col == other.col
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j] += other.get(i, j)
        return self

    def __isub__(self, other):
        assert self.row == other.row and self.col == other.col
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j] -= other.get(i, j)
        return self

    def __imul__(self, k):
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j] *= k
        return self