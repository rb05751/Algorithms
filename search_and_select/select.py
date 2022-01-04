"""Non-randomized version of SELECT to find ith order statistic in an Array A"""

from typing import *
import copy
from sorting.insertion_sort import InsertionSort

Array = List[float]


class Select:
    def __init__(self, items: Array, order: int):
        self.items = items
        self.ith = order

    def __divide(self) -> List[float]:
        """divides items into groups of floor(n/5)"""
        items = copy.deepcopy(self.items)
        new_items = []
        for i in range(0, len(items), 5):
            if len(items[i:]) > 5: # if remainder is greater than subgroup size
                yield items[i:i+5]
            else:
                yield items[i:]

    def __find_median(self, items):
        if len(items) > 5:
            medians = []
            divided_items = self.__divide()
            for item in divided_items:
                sorter = InsertionSort(items=item, ascending=True)
                sorted_items = sorter.sort()
                median = sorted_items[len(sorted_items)//2]
                medians.append(median)
            return self.__find_median(items=medians)
        else:
            sorter = InsertionSort(items=items, ascending=True)
            sorted_items = sorter.sort()
            if len(sorted_items) == 3:
                idx = sorted_items[len(sorted_items) // 2]
            else:
                idx = sorted_items[len(sorted_items) // 2-1]
            return idx if len(sorted_items) > 2 else sorted_items[0]

    def __swap(self, A, idx1, idx2):
        temp = A[idx1]
        A[idx1] = A[idx2]
        A[idx2] = temp
        return A

    def __partition(self, items, q):
        if len(items) <= 1:
            return items, 0
        items = self.__swap(items, idx1=items.index(q), idx2=-1) # swap with last item in Array
        i = -1
        for j in range(len(items)):
            if items[j] <= q:
                i += 1
                items = self.__swap(A=items, idx1=i, idx2=j)

        ## swap q back to rightful position
        items = self.__swap(A=items, idx1=i+1, idx2=-1)
        return items, i

    def select(self, items, k):
        median = self.__find_median(items)
        new_items, partition_idx = self.__partition(items=items, q=median)
        if partition_idx == k-1:
            return new_items[partition_idx]
        elif partition_idx > k-1:
            return self.select(items=new_items[:partition_idx], k=k)
        else:
            return self.select(items=new_items[partition_idx+1:], k=k-partition_idx-1)

if __name__ == '__main__':
    items = [3, 4, 7, 1, 5, 8, 9]
    order = 9
    select = Select(items=items, order=order)
    print(select.select(items, k=order))
    print(list(sorted(items))[order-1])
