"""
Longest Common Subsequence is a classic dynamic programming problem where you are given 2 strings X & Y and the goal
is to compute the longest subsequence that exists in both X & Y. For example:

X = ABCBDAB
Y = BDCABA

LCS = BCBA or BDAB

Optimal Substructure:

- If X[i] == Y[j], then LCS(X[:i], Y[:j]) = LCS(X[:i-1], Y[:i-1]) + X[i]
- Else:
    - LCS = max( LCS(X[:i-1], Y[:j]) , LCS(X[:i], Y[:j-1]) )

Proof (By Contradiction):

m = len(X)
n = len(Y)

1. If X[m] == Y[n]:
    - Assumption: Lets assume we that had an LCS called Z[1...k] of X & Y and Z[k] (it's last element) is not equal to X[m]=Y[n]
    - We could then take X[m]=Y[n] and append it to Z, producing an LCS of length k + 1
    - Which contradicts our original assumption that Z[1...k] was an LCS of X & Y
    - Also, suppose that there is an LCS (W) of X[:m-1] Y[:n-1], and W's length is greater than k - 1.
    - We could then append X[m]=Y[n] to Z and produce a common subsequence longer than Z. Contradicting our assumption
        on Z's optimality, again!
    - Thus, if X[i]==Y[j], the LCS is the LCS(X[:i-1], Y[:j-1]) + X[i] (or Y[j])

2. If Z[k] not equal to X[m]
    - Assumption: Z is an LCS of X[:m-1], Y[j] & thus X & Y
    - Lets imagine there is an even longer common subsequence (W) of X[:m-1] Y[:n] and it has length greater than Z.
    - This means W is also an LCS of all of X & Y, contradicting our assumption that Z was an LCS of X & Y.

3. If Z[k] not equal to Y[n]: symmetric to # 2
"""

import numpy as np


class LCS:
    def __init__(self, X, Y):
        self.X = ['<START>'] + X
        self.Y = ['<START>'] + Y
        self.length_table = np.zeros(shape=(len(X) + 1, len(Y) + 1))
        self.seq_table = np.zeros(shape=(len(X), len(Y)))

    def fill_in_tables(self):
        for i in range(1, self.length_table.shape[0]):
            for j in range(1, self.length_table.shape[1]):
                if self.X[i] == self.Y[j]:
                    self.length_table[i, j] = self.length_table[i - 1, j - 1] + 1
                    self.seq_table[i - 1, j - 1] = 3
                elif self.length_table[i, j - 1] > self.length_table[i - 1, j]:
                    self.length_table[i, j] = self.length_table[i, j - 1]
                    self.seq_table[i - 1, j - 1] = 2
                else:
                    self.length_table[i, j] = self.length_table[i - 1, j]
                    self.seq_table[i - 1, j - 1] = 1

    def construct_optimal_solution(self):
        X, Y = self.X[1:], self.Y[1:]
        subsequence = []
        i, j = self.seq_table.shape[0] - 1, self.seq_table.shape[1] - 1

        while True:
            if i == -1 or j == -1:
                break
            elif self.seq_table[i, j] == 1:
                i -= 1
            elif self.seq_table[i, j] == 2:
                j -= 1
            else:
                subsequence.insert(0, X[i])
                i -= 1
                j -= 1

        return subsequence

    def run(self):
        # 1. Run Algo - Fill-in tables
        self.fill_in_tables()

        # 2. Construct Optimal Solution
        solution = self.construct_optimal_solution()

        return solution


if __name__ == '__main__':
    # 1. Create examples
    X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    Y = ['B', 'D', 'C', 'A', 'B', 'A']

    lcs = LCS(X=X, Y=Y)
    result = lcs.run()

    print(f"Length of LCS: {len(result)}")
    print(f"LCS: {result}")
