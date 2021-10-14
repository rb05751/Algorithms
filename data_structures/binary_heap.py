import copy
import random


class BinaryHeap:
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

    def increase_key(self, i, key, value=None):
        A = copy.deepcopy(self.items)
        if i < len(A):
            if key < list(A[i].keys())[0]:
                return "Key is less than element in array therefore there is no increment"
            A[i] = {key: value} if value is not None else {key: list(A[i].values())[0]}
            if self.priority == "max":
                while i > 0 and (list(A[i // 2-1].keys())[0] < list(A[i].keys())[0]):
                    A[i] = A[i//2-1]
                    i = i // 2-1

                A[i] = {key: value} if value is not None else {key: list(A[i].values())[0]}
                self.items = A
            else:
                A[i] = {key: value} if value is not None else {key: list(A[i].values())[0]}
                self.items = self.heapify(A, i)
        else:
            return A


    def insert(self, key, value):
        self.items.append({float('-inf'): value})  # O(1)
        self.increase_key(i=len(self.items) - 1, key=key)

    def build_heap(self):
        A = copy.deepcopy(self.items)
        if self.priority == "max":
            for i in range(self.n // 2 - 1, -1, -1):
                A = self.heapify(A, i)
        else:
            for i in range(self.n //2 - 1, -1, -1):
                A = self.heapify(A, i)
        self.items = A

    def heapify(self, A, i):
        largest = None
        if self.priority == "max":
            l = 2 * i + 1
            r = 2 * i + 2
            if l <= len(A) - 1 and list(A[l].keys())[0] > list(A[i].keys())[0]:
                largest = l
            else:
                largest = i

            if r <= len(A) - 1 and list(A[r].keys())[0] > list(A[largest].keys())[0]:
                largest = r

            if largest != i:
                self.__swap(A, i, largest)
                return self.heapify(A, largest)
            else:
                return A
        else:
            smallest = None
            l = 2 * i + 1
            r = 2 * i + 2
            if l <= len(A) - 1 and list(A[l].keys())[0] < list(A[i].keys())[0]:
                smallest = l
            else:
                smallest = i

            if r <= len(A) - 1 and list(A[r].keys())[0] < list(A[smallest].keys())[0]:
                smallest = r

            if smallest != i:
                self.__swap(A, i, smallest)
                return self.heapify(A, smallest)
            else:
                return A



if __name__ == '__main__':
    items = [{3: 'Dog'}, {2: 'Cat'}, {1: 'Bob'}, {6:'Sally'}, {4: 'Harry'}, {7: 'Lizard'}, {5: 'Frog'}]
    print(items)
    queue = BinaryHeap(items=items, priority="min")
    queue.build_heap()
    print(queue.items)
    queue.increase_key(2, 9)
    print(queue.items)