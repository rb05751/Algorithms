"""
In the Optimal BST problem, you are given a set of keys with an associate search probability along with a set of dummy keys
that represent searches for numbers less than and/or equal to each key. Your goal is to construct a tree such that the
expected search cost is minimized.

Optimal Substructure:

Let:

- A = set of keys
- P = search probabilities for each key
- D = search probabilities for values not covered by those keys (the intervals in b/t and to neg. inf and pos. inf)
- r = a key chosen as root

OPT-BST-COST(A[i...j]) = min(r)[i...j] { OPT-BST-COST(A[i...r-1]) + OPT-BST-COST(A[r+1...j]) + sum(P[i...j] + D[i-1...j]) }

Proof:

- Assumption: We have an optimal BST (T) that has subtree T' containing keys A[i....j], then this subtree (T') must be
    optimal as well for the subproblem with keys A[i...j] and dummy keys i-1...j.

- Lets imagine we had an even more optimal subtree T'' on the keys A[i...j] and dummy keys i-1...j.
- We could then cut out the subtree T' and replace it with T'' producing a more optimal solution to T, contradicting
    our original optimality assumption for T.

- Thus, the subtrees of T must be optimal on their respective range of keys & dummy keys.

"""

import numpy as np


class OptimalBST:
    def __init__(self, num_keys, key_probs, dummy_probs):
        self.num_keys = num_keys
        self.key_probs = key_probs
        self.dummy_probs = dummy_probs

        # Initialize tables
        self.expected_search_cost = np.full((num_keys + 1, num_keys + 1), np.inf)
        self.prob_table = np.full((num_keys + 1, num_keys + 1), np.inf)
        self.root_table = np.full((num_keys, num_keys + 1), np.inf)

    def init_tables(self):
        for i in range(self.num_keys + 1):
            self.expected_search_cost[i, i] = dummy_probs[i]
            self.prob_table[i, i] = dummy_probs[i]

    def fill_in_tables(self):
        for tree_size in range(1, num_keys + 1):
            for i in range(num_keys - tree_size + 1):
                j = i + tree_size
                self.prob_table[i, j] = self.prob_table[i, j - 1] + key_probs[j] + dummy_probs[j]
                for root_num in range(i, j):
                    tree_cost = self.expected_search_cost[i, root_num] + self.expected_search_cost[root_num + 1, j] + \
                                self.prob_table[
                                    i, j]
                    if tree_cost < self.expected_search_cost[i, j]:
                        self.expected_search_cost[i, j] = tree_cost
                        self.root_table[i, j] = root_num

    def construct_optimal_bst(self, i, j, parent, relation):
        if abs(i - j) == 0:
            return
        if abs(i - j) == 1:
            print(f"{int(self.root_table[i, j])} is the {relation} of {parent}")
            return
        else:
            if parent is None:
                r = int(self.root_table[i, j])
                print(f"{r} is the root")
            else:
                r = int(self.root_table[i, j])
                print(f"{r} is the {relation} of {parent}")

            self.construct_optimal_bst(i=i, j=r, parent=r, relation='left child')
            self.construct_optimal_bst(i=r + 1, j=j, parent=r, relation='right child')

    def run(self):
        self.init_tables()
        self.fill_in_tables()

        # Print optimal solution
        print("Search cost table:\n")
        print(self.expected_search_cost)
        print("-----------------------------")
        print("Tree structure:\n")
        self.construct_optimal_bst(i=0, j=self.num_keys, parent=None, relation=None)


if __name__ == '__main__':
    # 1. Define inputs
    num_keys = 5
    key_probs = [0, 0.15, 0.10, .05, .10, .20]
    dummy_probs = [.05, .10, .05, .05, .05, .10]

    optimal_bst = OptimalBST(num_keys=num_keys, key_probs=key_probs, dummy_probs=dummy_probs)
    optimal_bst.run()
