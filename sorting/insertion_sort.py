class InsertionSort:
    def __init__(self, items, ascending=True):
        self.items = items
        self.n = len(items)
        self.asc = ascending

    def sort(self):
        if self.asc:
            for j in range(1, self.n):
                key = self.items[j]
                i = j - 1
                while i > -1 and self.items[i] > key:
                    self.items[i+1] = self.items[i]
                    i = i - 1
                self.items[i+1] = key
        else:
            for j in range(1, self.n):
                key = self.items[j]
                i = j - 1
                while i > -1 and self.items[i] < key:
                    self.items[i+1] = self.items[i]
                    i = i - 1
                self.items[i+1] = key

        return self.items


if __name__ == "__main__":
    num_list = [5, 2, 4, 6, 1, 3, 5, 5]
    Isorter = InsertionSort(items=num_list, ascending=True)
    print(f"Unsorted list: {num_list}")
    print(f"Sorted list: {Isorter.sort()}")
