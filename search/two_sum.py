"""Objective of this algorithm is to determine if there are two items in a set of integers S of length (n)
that's sum is equal to some desired value X."""

from sorting.merge_sort import MergeSort


class TwoSum:
    def __init__(self, items, X):
        self.items = items
        self.X = X
        self.n = len(items)
        self.sorter = MergeSort(self.items)

    def run(self):
        A = self.sorter.run()
        i = 0
        j = self.n - 1

        while i <= j:
            if A[i] + A[j] == self.X:
                return True
            elif A[i] + A[j] < self.X:
                i += 1
            else:
                j += 1

        return False


if __name__ == "__main__":
    num_list = [5, 2, 4, 6, 1, 3, 3, 8, 9, 11, 7, 0, 1, 4, 10, 12]
    find_sum = TwoSum(items=num_list, X=17)
    print(find_sum.run())
