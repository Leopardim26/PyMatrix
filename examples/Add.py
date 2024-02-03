class Matrix:
    def __init__(self,rows, cols):
        self.row_ = rows
        self.col_ = cols

        for i in range(self.row_):
            for o in range(self.col_):
                self.matrix_[i][o] = 0

    def get(self,row,col):
        return self.matrix_[row][col]

    def set(self,row,col,value):
        if self.row_ == row and self.col_ == col:
            self.matrix_[row][col] = value

    def __add__(self, second):
        if self.row_ == second.row() and self.col_ == second.col():
            for i in range(self.row_):
                for o in range(self.col_):
                    set(i,o, self.matrix_[i][o]+second.get(i,o))

    def __sub__(self, second):
        if self.row_ == second.row() and self.col_ == second.col():
            for i in range(self.row_):
                for o in range(self.col_):
                    set(i,o, self.matrix_[i][o]-second.get(i,o))

    def __mul__(self, second):
        if self.col_ == second.row():
            temp = Matrix(self.row_, second.col())
            for i in range(self.row_):
                for o in range(second.col()):
                    for e in range(second.row()):
                        temp.set(i,o, temp.get(i,o)+self.matrix_[i][e]*second.get(e,o))
            return temp

    def __eq__(self,second):
        if self.row_ == second.row() and self.col_ == second.col():
            for i in range(self.row_):
                for o in range(self.col_):
                    set(i,o, second.get(i,o))

    def t(self):
        temp = Matrix(self.col_,self.row_)
        for i in range(self.row_):
            for o in range(self.col_):
                temp.set(o,i, self.matrix_[i][o])

    def i(self):
        temp = Matrix(self.row_, self.col_)
        if self.row_ == 1 and self.col_ == 1:
            self.matrix_[0][0] = self.matrix_[0][0]*-1
        elif self.row_ == 2 and self.col_ == 2:
            det = self.get(0,0) * self.get(1,1) - self.get(1,0) * self.get(0,1)
            temp.set(0,0, self.get(0,0)/det)
            temp.set(0,1, -self.get(0,1)/det)
            temp.set(1,1, self.get(1,1)/det)
            temp.set(1,0, -self.get(1,0)/det)

    def print(self):
        for i in range(self.row_):
            for o in range(self.col_):
                t+= str(self.matrix_[o][i])
            print(t)

    def row(self):
        return self.row_
    
    def col(self):
        return self.col_

A = Matrix(1,2)
A.set(0,0,1)
A.set(0,1,2)

B = Matrix(1,2)
B.set(0,0,5)
B.set(0,1,7)

C = Matrix(1,2)

C == A+B

C.print()