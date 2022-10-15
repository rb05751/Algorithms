"""
In 0-1 knapsack, you are given N items with some value (v) and weight (w) and your goal is to fill up a knapsack
of capacity (W) with the maximum value possible. You can only choose whole items not fractional ones.

Algorithm:

1. Construct a table (S) of size N+1 x W+1.
2. Fill-in 0 column & 0 row with 0's because this corresponds to having either 0 items or 0 capacity.
3. In row-major order starting with item 1:
    if w(i) > W:
        S[i,w] = S[i-1,w] // leave it out because it could never fit
    else:
        S[i,w] = MAX( S[i-1, w-w(i)] + v(i)  , S[i-1, w]

Optimal Substructure:

S[i,w] = MAX( S[i-1, w-w(i)] + v(i)  , S[i-1, w]

Proof:

- Assume an optimal solution to S[i,w] that consists of S[i-1, w-w(i)] + v(i).
- Imagine we found a higher value set of items to fill w-w(i)
- We could cut out our current set & replace it with this new set & construct an even more optimal solution.
- Contradiction. Thus, S[i,w] must consist of an optimal solution to S[i-1, w-w(i)]

RUNNING TIME: O(NW)
"""
import numpy as np


class KnapSack:
    def __init__(self, items, max_capacity):
        self.items = items
        self.N = len(items)
        self.W = max_capacity
        self.S = np.zeros((2, self.W + 1))

    def compute(self):
        for i in range(1, N + 1):
            current_item = items[i - 1]
            for j in range(1, W + 1):
                current_capacity = j
                current_item_weight = current_item['w']
                if current_item_weight <= current_capacity:
                    self.S[1, j] = max(self.S[0, current_capacity],
                                       self.S[0, current_capacity - current_item_weight] + current_item['v'])
                else:
                    self.S[1, j] = self.S[0, j]

            self.S[0, :] = self.S[1, :]
            self.S[1, :] = np.zeros((1, self.W + 1))

        return self.S


if __name__ == '__main__':
    items = [{'v': 5, 'w': 2}, {'v': 3, 'w': 2}, {'v': 6, 'w': 3}, {'v': 7, 'w': 2}]
    N = len(items)
    W = 5

    knapsack = KnapSack(items=items, max_capacity=W)
    solution_table = knapsack.compute()
    print(solution_table)
    print(f"Max Value Possible: {solution_table[0, W]}")
