class SelectionSort:
    def __init__(self, items):
        self.items = items
        self.n = len(items)

    def __pre_process(self):
        if self.n == 0:
            return False
        for i in range(1, len(self.items)):
            if self.items[i-1] > self.items[i]:
                return True
        return False

    def sort(self):
        if self.__pre_process():
            min_elem = [2e30, 2e30]
            for i, elem in enumerate(self.items):
                for j in range(i, len(self.items)):
                    if self.items[j] < min_elem[0]:
                        min_elem[0], min_elem[1] = self.items[j], j
                self.items[min_elem[1]] = self.items[i]
                self.items[i] = min_elem[0]
                min_elem = [2e30, 2e30]
        return self.items


if __name__ == "__main__":
    num_list = [5, 2, 4, 6, 1, 3, 5, 5]
    select_sorter = SelectionSort(items=num_list)
    print(f"Unsorted list: {num_list}")
    print(f"Sorted list: {select_sorter.sort()}")
