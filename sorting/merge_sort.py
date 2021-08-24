class MergeSort:
    def __init__(self, items):
        self.items = items
        self.n = len(items)

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

        if i < len(A):
            C.extend(A[i:])
        else:
            C.extend(B[j:])

        return C

    def sort(self, arr):
        print(arr)
        if len(arr) <= 1:
            return arr
        else:
            n = len(arr)
            A = self.sort(arr[:n // 2])
            B = self.sort(arr[n // 2:])
            C = self.merge(A, B)
        return C

    def run(self):
        return self.sort(arr=self.items)


if __name__ == "__main__":
    num_list = [5, 2, 4, 6, 1, 3, 3, 8, 9, 11, 7, 0, 1, 4, 10, 12]
    merger = MergeSort(items=num_list)
    print(merger.run())
