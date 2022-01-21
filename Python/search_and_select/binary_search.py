from Python.sorting import insertion_sort


class BinarySearch:
    def __init__(self, items):
        self.items = items

    def sort(self):
        sorter = insertion_sort.InsertionSort(self.items, ascending=True)
        self.items = sorter.sort()

    def search(self, arr, v, i, idx_adj=0):
        print(f"This is arr: {arr} and this is i: {i} and this is v: {v}")
        if len(arr) == 1:
            if arr[0] == v:
                return True, i + idx_adj - 1
            else:
                return False, None
        else:
            if arr[i // 2] == v:
                return True, i // 2 + idx_adj
            elif arr[i // 2] < v:
                return self.search(arr[i // 2 + 1:], v, i=i - i // 2, idx_adj=i // 2 + 1)
            else:
                return self.search(arr[:i // 2], v, i=i // 2, idx_adj=idx_adj)

    def run(self, v):
        self.sort()
        return self.search(arr=self.items, v=v, i=len(self.items))


if __name__ == "__main__":
    num_list = [5, 2, 4, 6, 1, 3, 3, 8, 9, 11, 7, 10, 12]
    Bsearch = BinarySearch(items=num_list)
    print(Bsearch.run(v=3))
