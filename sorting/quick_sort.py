import random
import copy


class QuickSort:
    def __init__(self, items, is_random=False, ascending=True):
        self.items = items
        self.n = len(items)
        self.is_random = is_random
        self.ascending = ascending

    def check(self, A):
        if len(A) != 0:
            last = A[0]
            for i in range(1, len(A)):
                if A[i] != last:
                    return True
                else:
                    continue
            return False
        else:
            return False

    def __swap(self, A, idx1, idx2):
        temp = A[idx1]
        A[idx1] = A[idx2]
        A[idx2] = temp
        return A

    def reg_partition(self, A):
        """Takes in an array or list (A) and returns Q and index to partition the list/array on"""
        if self.is_random:
            idx = random.randint(0, len(A) - 1)
        else:
            idx = -1
        pivot = A[idx]
        self.__swap(A, idx1=idx, idx2=-1)
        i = -1

        if self.ascending:
            for j in range(len(A) - 1):
                if A[j] <= pivot:
                    i += 1
                    A = self.__swap(A, idx1=j, idx2=i)

            A = self.__swap(A, idx1=i + 1, idx2=-1)
        else:
            for j in range(len(A) - 1):
                if A[j] >= pivot:
                    i += 1
                    A = self.__swap(A, idx1=j, idx2=i)

            A = self.__swap(A, idx1=i + 1, idx2=-1)

        return A, i + 1

    def sort(self, A):
        if len(A) <= 1:
            return A
        else:
            A, q = self.reg_partition(A)
            return self.sort(A[:q]) + [A[q]] + self.sort(A[q + 1:])


if __name__ == '__main__':
    num_list = [5, 2, 4, 6, 1, 3, 3, 8, 9, 11, 7, 0, 1, 4, 10, 12]
    sorter = QuickSort(items=num_list, is_random=False, ascending=True)
    if sorter.check(A=num_list):
        print(sorter.sort(num_list))
    else:
        print(num_list)
