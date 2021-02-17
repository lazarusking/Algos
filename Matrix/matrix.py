class Matrix:

    def __init__(self, l, b):
        self.l = l
        self.b = b
# check if matrix is lower triangular(0s above diagonal)

    def isLowerTriangular(self):
        for i in range(0, len(self.l)):
            for j in range(i+1, len(self.l)):
                if(self.l[i][j]) != 0:
                    return False
        return True
# check if matrix is upper triangular(0s below diagonal)

    def isUpperTriangular(self):
        for i in range(1, len(self.l)):
            for j in range(0, i):
                if(self.l[i][j]) != 0:
                    return False
        return True
# Algorithm for solving forward_substitution

    def forward_sub(self):
        n = len(self.b)
        x = [0]
        x[0] = self.b[0]/self.l[0][0]  # first row contains first x1
        for m in range(1, n):  # loop from second row to last
            sum = 0
            for i in range(m):  # loop in current row to outer loop count to not encounter 0
                sum += self.l[m][i]*x[i]
            xm = (self.b[m]-sum)/self.l[m][m]
            x.append(xm)

        print(f"Forward Substitution")

        print(f"Lx \t =  B")

        for i in range(n):
            for j in range(n):
                if type(self.l[i][j]) == float and (self.l[i][j] != 0):
                    self.b[i] = float(f"{self.b[i]:.2f}")
                    self.l[i][j] = float(f"{self.l[i][j]:.2f}")
                t = " "  # whitespace
            if i == 0:
                print(f"{self.l[i]}  \t{t*i}\t {x[i]:>5}\t= {self.b[i]:>10}")
            else:
                print(f"{self.l[i]}  {t*2*i}\t {x[i]:>5}\t= {self.b[i]:>10}")

# Algorithm for solving backward_substitution

    def backward_sub(self):
        n = len(self.b)
        x = [0 for x in range(n)]
        # last row contains first x1
        x[n-1] = round(self.b[n-1]/self.l[n-1][n-1], 3)

        for m in range(n-1, 0, -1):  # loop from last-but-one row to first
            sum = 0
            for i in range(n-1, m-1, -1):
                # loop in row n-1(last but one)row
                # to outer loop count to not encounter 0
                sum += self.l[m-1][i]*x[i]
            xm = round((self.b[m-1]-sum)/self.l[m-1][m-1], 2)
            x[m-1] = xm
            # row -= 1

        # print(x)
        print(f"\nBackward Substitution")
        # for i in range(n):
        #     mat = self.l[i]
        #     print(f"{self.l[i]}")
        # print(f"\n x \t B")
        # for i in range(n):

        print(f"Lx \t = B")
        #     print(f" {x[i]} \t{self.b[i]}")
        for i in range(n):
            for j in range(n):
                if type(self.l[i][j]) == float and (self.l[i][j] != 0):
                    self.b[i] = float(f"{self.b[i]:.2f}")
                    self.l[i][j] = float(f"{self.l[i][j]:.2f}")
                t = " "  # whitespace
            if i == 0:
                print(f"{self.l[i]}  \t{t*i}\t {x[i]:>5}\t= {self.b[i]:>10}")
            else:
                print(f"{self.l[i]}  {t*2*i}\t {x[i]:>5}\t= {self.b[i]:>10}")

        #     # print(f"{self.l[i]}\t {x[i]} \t{self.b[i]}")
        # for i in range(n):
        #     t = " "
        #     if i == 0:
        #         print(f"{self.l[i]}  \t{t*i}\t {x[i]:>5}\t= {self.b[i]:>10}")
        #     else:
        #         print(f"{self.l[i]}  {t*2*i}\t {x[i]:>5}\t= {self.b[i]:>10}")

        #     print(f" {x[i]} \t{self.b[i]}")

    #  Lx=b
    #   L             x     b
    # [[16, 0, 0, 0], x1   16,
    #  [5, 11, 0, 0], x2   27,
    #  [9, 7, 6, 0],  x3   41,
    #  [4, 14, 15, 1],x4   81]


def main():
    L = [[16, 0, 0, 0],
         [5, 11, 0, 0],
         [9, 7, 6, 0],
         [4, 14, 15, 1]]

    b = [16, 27, 41, 81]

    # A = [[16, 2, 3, 13],
    #      [0, 11, 10, 8],
    #      [0, 0, 6, 12],
    #      [0, 0, 0, 1]]

    # y = [81, 53, 60, 3]
    A = [[4, 1, -1, 1, -1],
         [0, -7/2, 9/2, 1/2, -9/2],
         [0, 0, 89/14, -11/7, 1/7],
         [0, 0, 0, 170/89, 25/89],
         [0, 0, 0, 0, -189/34]]

    y = [0, 6, 9/14, 183/356, 4833/680]
    print("Examples")
    print("----------")
    matrix = Matrix(L, b)
    if(matrix.isUpperTriangular()):
        matrix.backward_sub()
    elif(matrix.isLowerTriangular()):
        matrix.forward_sub()
    else:
        print("Invalid Matrix")

    matrix = Matrix(A, y)
    if(matrix.isUpperTriangular()):
        matrix.backward_sub()
    elif(matrix.isLowerTriangular()):
        matrix.forward_sub()
    else:
        print("Invalid Matrix")

    n = int(input("\nEnter the matrix dimensions:"))
    x = [[int(input("Enter a matrix A:")) for i in range(n)] for y in range(n)]
    b = [int(input("Enter the resultant matrix:")) for y in range(n)]
    print(x)
    print(b)
    matrix = Matrix(x, b)
    if(matrix.isUpperTriangular()):
        matrix.backward_sub()
    elif(matrix.isLowerTriangular()):
        matrix.forward_sub()
    else:
        print("Invalid Matrix")


if __name__ == "__main__":
    main()
