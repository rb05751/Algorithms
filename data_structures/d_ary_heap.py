import copy
import random


class BinaryHeap:
    """An implementation of priority queue using a Heap"""

    def __init__(self, d, items, priority="max"):
        self.items = items
        self.priority = priority
        self.n = len(items)
        self.d = d

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
                while i > 0 and (list(A[i // self.d-1].keys())[0] < list(A[i].keys())[0]):
                    A[i] = A[i//self.d-1]
                    i = i // self.d-1

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
        for i in range(self.n // 2, -1, -1):
            A = self.heapify(A, i)
        self.items = A

    def heapify(self, A, i):
        if self.priority == "max":
            # Gives a list of d children
            children = list(filter(lambda x: x is not None, [[A[self.d * i + j],int(self.d * i + j)]  if int(self.d * i + j) < len(A) else None for j in range(1,self.d+1)]))
            if len(children) > 0: # check if we actually have children
                largest = list(sorted(children, key=lambda x: list(x[0].keys())[0], reverse=True))[0]
                if list(largest[0].keys())[0] > list(A[i].keys())[0]:
                    self.__swap(A, i, largest[1])
                    return self.heapify(A, largest[1]) # recurse on largest
                else:
                    return A
            else:
                return A
        else:
            # Gives a list of d children
            children = list(filter(lambda x: x is not None, [[A[self.d * i + j],int(self.d * i + j)]  if int(self.d * i + j) < len(A) else None for j in range(1,self.d+1)]))
            if len(children) > 0: # check if we actually have children
                smallest = list(sorted(children, key=lambda x: list(x[0].keys())[0]))[0]
                if list(smallest[0].keys())[0] < list(A[i].keys())[0]:
                    self.__swap(A, i, smallest[1])
                    return self.heapify(A, smallest[1]) # recurse on smallest
                else:
                    return A
            else:
                return A



if __name__ == '__main__':
    items = [{3: 'Dog'}, {2: 'Cat'}, {1: 'Bob'}, {6:'Sally'}, {4: 'Harry'}, {7: 'Lizard'}, {5: 'Frog'}]
    print(items)
    queue = BinaryHeap(items=items, d=2, priority="min")
    queue.build_heap()
    print(queue.items)