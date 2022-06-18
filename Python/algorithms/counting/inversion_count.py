from algorithms.sorting.merge_sort import MergeSort


class CountInversions(MergeSort):
    def __init__(self, items):
        super().__init__(items)
        self.total = 0

    def merge(self, A, B):
        i = 0
        j = 0
        C = []
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
                self.total += len(A[i:])

        if i < len(A):
            C.extend(A[i:])
        else:
            C.extend(B[j:])

        return C


if __name__ == "__main__":
    num_list = [5, 2, 4, 6, 1, 3, 3, 8, 9, 11, 7, 0, 1, 4, 10, 12]
    num_list = [5,4,3,2,1]
    inversion_counter = CountInversions(items=num_list)
    print(inversion_counter.run())
    print(inversion_counter.total)
