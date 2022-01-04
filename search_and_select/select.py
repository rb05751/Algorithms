"""Non-randomized version of SELECT to find ith order statistic in an Array A"""

from typing import *
import copy
from sorting.insertion_sort import InsertionSort

Array = List[float]


class Select:
    def __init__(self, items: Array):
        self.items = items

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
            return sorted_items[len(sorted_items) // 2]  if len(sorted_items) > 2 else sorted_items[0]



    def compute(self):
        return self.__find_median(items=self.items)

if __name__ == '__main__':
    import statistics
    items = [3, 4, 7, 1, 5, 8, 9]
    select = Select(items=items)
    print(select.compute())
