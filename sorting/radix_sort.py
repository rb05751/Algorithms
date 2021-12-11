class RadixSort:
    """Note: only handles positive integers"""
    def __init__(self, items, ascending=False):
        self.items = items
        self.max_length_digit = None
        self.ascending = ascending

    def pre_process_items(self):
        self.max_length_digit = max([len(str(self.items[i])) for i in range(len(self.items))])
        for i, num in enumerate(self.items):
            num_list = [int(str(num)[j]) for j in range(len(str(num)))]
            self.items[i] = [0]* (self.max_length_digit - len(str(num))) + num_list

    def post_process_items(self):
        C = []
        for i, num in enumerate(self.items):
            for j in range(len(num)):
                if self.items[j] != 0:
                    self.items[i] = "".join([str(self.items[i][k]) for k in range(len(self.items[i]))])
                    C.append(int(self.items[i]))

        return C

    def compute(self):
        if len(self.items) > 0:
            self.pre_process_items()
            for i in range(self.max_length_digit-1, -1, -1):
                self.items = list(sorted(self.items, key=lambda x: x[i], reverse=self.ascending))

            self.items = self.post_process_items()
            return self.items
        else:
            return []

if __name__ == '__main__':
    items = [2,5,3,0,2,3,0,3]
    radix_sort = RadixSort(items=items)
    sorted_items = radix_sort.compute()
    print(sorted_items)