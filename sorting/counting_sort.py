

class CountingSort:
    def __init__(self, items):
        self.A = items
        if len(items) > 0:
            self.B = [0]*len(self.A)
            self.C = [0]*(max(self.A)+1)
            self.k = max(self.A)
        else:
            self.B = [0] * len(self.A)
            self.C = []
            self.k = None

    def build_c(self):
        for i in range(len(self.A)):
            self.C[self.A[i]] += 1

        for i in range(1, self.k+1):
            self.C[i] += self.C[i-1]

    def compute(self):
        if len(self.A) > 0:
            self.build_c()
            for j in range(len(self.A)-1, -1, -1):
                self.B[self.C[self.A[j]]-1] = self.A[j]
                self.C[self.A[j]] -= 1
            return self.B
        else:
            return []

if __name__ == '__main__':
    items = [2,5,3,0,2,3,0,3]
    count_sort = CountingSort(items=items)
    sorted_items = count_sort.compute()
    print(sorted_items)

