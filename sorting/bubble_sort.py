"""Bubble sort implementation: running time == O(n^2)"""
import copy

class BubbleSort:
    def __init__(self, items):
        self.items = items
        self.n = len(items)

    def run(self):
        A = copy.deepcopy(self.items)
        for i in range(self.n-1):
            for j in range(self.n-1, i, -1):
                if A[j] < A[j-1]:
                    temp = A[j]
                    A[j] = A[j-1]
                    A[j-1] = temp

        return A


if __name__=="__main__":
    num_list = [5, 2, 4, 6, 1, 3, 3, 8, 9, 11, 7, 0, 1, 4, 10, 12]
    bubble_sort = BubbleSort(items=num_list)
    print(bubble_sort.run())