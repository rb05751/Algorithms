import copy
import random


class HeapSort:
    def __init__(self, items, ascending=True):
        self.items = items
        self.ascending = ascending
        self.n = len(items)

    def swap(self, A, idx1, idx2):
        temp = A[idx1]
        A[idx1] = A[idx2]
        A[idx2] = temp
        return A

    def build_max_heap(self):
        A = copy.deepcopy(self.items)
        for i in range(self.n // 2-1, -1, -1):
            A = self.max_heapify(A, i)

        return A

    def max_heapify(self, A, i):
        l = 2 * i + 1
        r = 2 * i + 2
        largest = None
        if l <= len(A)-1 and A[l] > A[i]:
            largest = l
        else:
            largest = i

        if r <= len(A)-1 and A[r] > A[largest]:
            largest = r

        if largest != i:
            A = self.swap(A, idx1=i, idx2=largest)
            return self.max_heapify(A, largest)
        else:
            return A

    def sort(self):
        A = self.build_max_heap()
        for i in range(len(A) - 1, 0, -1):
            A = self.swap(A, 0, i)
            A = self.max_heapify(A[:i], 0) + A[i:]

        return A


if __name__ == '__main__':
    items = [1, 2, 3, 3, 4, 7, 8, 2, 9, 10, 14, 16]
    random.shuffle(items)
    print(items)
    heap_sort = HeapSort(items)
    sorted_items = heap_sort.sort()
    print(sorted_items)
