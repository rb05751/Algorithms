import numpy as np
from Python.sorting.merge_sort import MergeSort


class YoungTableau:
    def __init__(self, items, m, n):
        self.sorter = MergeSort(items=items)
        self.items = self.sorter.run()
        self.m = m
        self.n = n
        self.T = None

    def find_inf(self):
        for i in range(self.T.shape[0]):
            for j in range(self.T.shape[1]):
                if self.T[i, j] == float('inf'):
                    return i, j

    def __swap(self, indices1, indices2):
        temp = self.T[indices2[0], indices2[1]]
        self.T[indices2[0], indices2[1]] = self.T[indices1[0], indices1[1]]
        self.T[indices1[0], indices1[1]] = temp

    def build_tableau(self):
        empty_matrix = np.zeros(shape=(self.m, self.n))
        ctr = 0
        for i in range(empty_matrix.shape[0]):
            for j in range(empty_matrix.shape[1]):
                if ctr < len(self.items):
                    empty_matrix[i, j] = self.items[ctr]
                    ctr += 1
                else:
                    empty_matrix[i, j] = float('inf')

        self.T = empty_matrix

    def insert(self, key):
        m, n = self.find_inf()
        self.T[m, n] = key
        found = False

        i = m
        j = n
        while not found:
            if i - 1 >= 0:
                top = self.T[i - 1, j]
            else:
                top = float('inf')
            if j - 1 >= 0:
                left = self.T[i, j - 1]
            else:
                left = float('inf')

            if left != float('inf') and top != float('inf'):
                if left > top and left > self.T[i, j]:
                    self.__swap(indices1=[i, j], indices2=[i, j - 1])
                    j -= 1
                elif top > left and top > self.T[i, j]:
                    self.__swap(indices1=[i, j], indices2=[i - 1, j])
                    i -= 1
                else:
                    found = True

            elif left != float('inf'):
                if left > self.T[i, j]:
                    self.__swap(indices1=[i, j], indices2=[i, j - 1])
                    j -= 1
                else:
                    found = True
            elif top != float('inf'):
                if top > self.T[i, j]:
                    self.__swap(indices1=[i, j], indices2=[i - 1, j])
                    i -= 1
                else:
                    found = True
            else:
                found = True

    def __find_last(self):
        for i in range(self.T.shape[0]):
            for j in range(self.T.shape[1] - 1):
                if self.T[i, j + 1] == float('inf') or (i + 1 > self.T.shape[0] and j + 1 > self.T.shape[1]):
                    return [i, j]

    def extract_min(self, i=0, j=0):
        min = self.T[i,j]
        """Start from root and swap element with smallest of neighbors,
        then recurse on that index. Halt when both neighbors are infinity"""
        if i < self.T.shape[0] and j < self.T.shape[1]:
            if self.T[i + 1, j] == self.T[i, j + 1] == float('inf'):
                self.T[i, j] = float('inf')
                return min
            elif self.T[i + 1, j] < self.T[i, j + 1]:
                self.__swap(indices1=[i, j], indices2=[i + 1, j])
                self.extract_min(i + 1, j)
            else:
                self.__swap(indices1=[i, j], indices2=[i, j + 1])
                self.extract_min(i, j + 1)
        elif i < self.T.shape[0]:
            if self.T[i + 1, j] == float('inf'):
                self.T[i, j] = float('inf')
                return min
            else:
                self.__swap(indices1=[i, j], indices2=[i + 1, j])
                self.extract_min(i + 1, j)
        else:
            if self.T[i, j + 1] == float('inf'):
                self.T[i, j + 1] = float('inf')
                return min
            else:
                self.__swap(indices1=[i, j], indices2=[i, j + 1])
                self.extract_min(i, j + 1)
        return min

if __name__ == '__main__':
    items = [9, 16, 3, 2, 4, 8, 5, 14, 12]
    young_tableau = YoungTableau(items, m=5, n=4)
    young_tableau.build_tableau()
    print(young_tableau.T)
    young_tableau.insert(1)
    print(young_tableau.T)
    print(young_tableau.extract_min())
    print(young_tableau.T)
