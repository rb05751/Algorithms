import copy
import random


class PriorityQueue:
    """An implementation of priority queue using a Heap"""

    def __init__(self, items, priority="max"):
        self.items = items
        self.priority = priority
        self.n = len(items)

    def __swap(self, A, idx1, idx2):
        temp = A[idx1]
        A[idx1] = A[idx2]
        A[idx2] = temp
        return A

    def get_top(self):
        A = copy.deepcopy(self.items)
        return A[0]

    def extract_top(self):
        A = copy.deepcopy(self.items)
        if len(A) < 1:
            return "Queue is empty"
        priority = A[0]
        A[0] = A[-1]
        A = A[:-1]
        self.items = self.heapify(A, 0)
        return priority

    def increase_key(self, i, key):
        A = copy.deepcopy(self.items)
        if key < A[i]:
            return "Key is less than element in array therefore there is no increment"
        if self.priority == "max":
            while i > 0 and (A[i // 2] < A[i]):
                A[i] = A[i//2]
                i = i // 2

            A[i] = key
            self.items = A
        else:
            pass

    def insert(self, key):
        self.items.append(float('-inf'))  # O(1)
        self.increase_key(i=len(self.items) - 1, key=key)

    def build_heap(self):
        A = copy.deepcopy(self.items)
        if self.priority == "max":
            for i in range(self.n // 2 - 1, -1, -1):
                A = self.heapify(A, i)
        else:
            pass
        self.items = A

    def heapify(self, A, i):
        largest = None
        if self.priority == "max":
            l = 2 * i + 1
            r = 2 * i + 2
            if l <= len(A) - 1 and A[l] > A[i]:
                largest = l
            else:
                largest = i

            if r <= len(A) - 1 and A[r] > A[largest]:
                largest = r

            if largest != i:
                self.__swap(A, i, largest)
                return self.heapify(A, largest)
            else:
                return A
        else:
            pass


if __name__ == '__main__':
    items = [1, 2, 3, 3, 4, 7, 8, 2, 9, 10, 14, 16]
    random.shuffle(items)
    print(items)
    queue = PriorityQueue(items=items, priority="max")
    queue.build_heap()
    print(queue.items)
    print(queue.extract_top())
    print(queue.items)
