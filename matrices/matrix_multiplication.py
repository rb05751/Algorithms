"""This module implements both the naive and Strassen's method for matrix multiplication for square matrices"""
import numpy as np

class MatrixMultiplier:
    def __init__(self, matrix_a, matrix_b):
        self.A = matrix_a
        self.B = matrix_b
        self.C = np.zeros((self.A.shape[0], self.B.shape[1]))
        self.n = self.A.shape[0]

    def split(self, matrix):
        """
        Splits a given matrix into quarters.
        Input: nxn matrix
        Output: tuple containing 4 n/2 x n/2 matrices corresponding to a, b, c, d
        """
        row, col = matrix.shape
        row2, col2 = row // 2, col // 2
        return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

    def strassen(self, x, y):
        """
        Computes matrix product by divide and conquer approach, recursively.
        Input: nxn matrices x and y
        Output: nxn matrix, product of x and y
        """

        # Base case when size of matrices is 1x1
        if len(x) == 1:
            return x * y

        # Splitting the matrices into quadrants. This will be done recursively
        # until the base case is reached.
        a, b, c, d = self.split(x)
        e, f, g, h = self.split(y)

        # Computing the 7 products, recursively (p1, p2...p7)
        p1 = self.strassen(a, f - h)
        p2 = self.strassen(a + b, h)
        p3 = self.strassen(c + d, e)
        p4 = self.strassen(d, g - e)
        p5 = self.strassen(a + d, e + h)
        p6 = self.strassen(b - d, g + h)
        p7 = self.strassen(a - c, e + f)

        # Computing the values of the 4 quadrants of the final matrix c
        c11 = p5 + p4 - p2 + p6
        c12 = p1 + p2
        c21 = p3 + p4
        c22 = p1 + p5 - p3 - p7

        # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
        c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
        print(c)
        return c

    def brute_force(self):
        C = np.zeros((self.A.shape[0], self.B.shape[1]))
        for i in range(self.C.shape[0]):
            for j in range(self.C.shape[1]):
                for k in range(C.shape[1]):
                    C[i][j] += self.A[i][k] * self.B[k][j]
        return C

    def run(self, test=False):
        strass = self.strassen(x=self.A, y=self.B)
        if test:
            brute = self.brute_force()
            return strass, brute
        return strass


if __name__ == '__main__':
    m_a = np.array([[1,3,4,1],
                    [2,2,5,1],
                    [2,1,3,2],
                    [3,4,1,2]])
    m_b = np.array([[2,1,4,1],
                    [2,5,3,1],
                    [2,0,4,2],
                    [1,3,1,4]])

    multiplier = MatrixMultiplier(matrix_a=m_a, matrix_b=m_b)
    print(multiplier.run())
