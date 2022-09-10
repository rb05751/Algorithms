"""
The goal of Matrix-Chain Multiplication is to find an optimal parenthesization of a chain of matrices, such that when
you multiply all of the matrices, abiding by this parenthesization, you get the lowest number of scalar multiplications.

Optimal substructure lemma:

OPT_P(A[i...j]) = min[k](i....j) { OPT_P(A[i...k]) + OPT_P(A[k+1...j]) + (A[i].Rows * A[k].Columns * A[j].Columns) }

Proof:

- Imagine that for some A[i...j] we had found a partitioning of A[i...k] and A[k+1....j] that is most optimal for A[i...j].

- If we had another A[i...k] that had a lower cost (more optimal) parenthesization, then we could replace our current partitioning
  of A[i...k] with this more optimal one and construct an even more optimal solution to A[i....j], thus contradicting our
  purported optimality of our original partition for A[i...j].

"""

import numpy as np


class MatrixChain:
    def __init__(self, matrix_table):
        self.matrix_table = matrix_table
        self.COST = np.zeros(shape=(len(matrix_table), len(matrix_table)))
        self.CUT = np.zeros(shape=(self.COST.shape[0], self.COST.shape[1]))

    def find_optimal_parenthesization(self):
        for chain_length in range(2, self.COST.shape[0] + 1):
            for i in range(self.COST.shape[0] - chain_length + 1):
                j = i + chain_length - 1
                optimal_cut, cut_index = float('inf'), -1
                for k in range(i, j):
                    p, q, r = self.matrix_table[str(i + 1)][0], self.matrix_table[str(k + 2)][0], self.matrix_table[str(j + 1)][1]
                    cost_of_cut = self.COST[i, k] + self.COST[k + 1, j] + (p * q * r)
                    if cost_of_cut < optimal_cut:
                        optimal_cut = cost_of_cut
                        cut_index = k

                # record optimal cuts
                self.COST[i, j] = optimal_cut
                self.CUT[i, j] = cut_index

    def find_solution(self, i, j):
        i, j = int(i), int(j)
        if j - i <= 2:
            if self.CUT[i,j] == i:
                return
            else:
                self.cut_sequence.insert(0, self.CUT[i, j])
                return
        else:
            next_cut = self.CUT[i, j]
            self.cut_sequence.insert(0, self.CUT[i, j])
            self.find_solution(i=next_cut + 1, j=j)
            self.find_solution(i=i, j=next_cut)

    def run(self):
        # 1. run algorithm
        self.find_optimal_parenthesization()

        # 2. find solution
        self.cut_sequence = []
        self.find_solution(i=0, j=self.COST.shape[0] - 1)
        self.cut_sequence = list(sorted(self.cut_sequence))

        # 3. print solution
        print(f"Optimal Cut Sequence: {self.cut_sequence}")
        print(f"Cost of Computation: {self.COST[0, self.COST.shape[1] - 1]}")


if __name__ == '__main__':
    # 1. Build matrix table
    matrix_table = {'1': [30, 35], '2': [35, 15], '3': [15, 5], '4': [5, 10], '5': [10, 20], '6': [20, 25]}

    # 2. Run it
    if len(matrix_table) >= 1:
        matrix_chain = MatrixChain(matrix_table=matrix_table)
        matrix_chain.run()
