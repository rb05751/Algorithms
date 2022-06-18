from algorithms.sorting.insertion_sort import InsertionSort


class BucketSort:
    def __init__(self, items, ascending=False):
        self.items = items
        self.hash_table = []
        self.ascending = ascending
        self.max_item = None

    def pre_process_items(self):
        self.max_item = max(self.items)
        new_list = [self.items[i] / self.max_item for i in range(len(self.items))]
        return new_list

    def bucket_items(self):
        self.hash_table = [[] for _ in range(10)]
        new_list = self.pre_process_items()
        for i in range(len(self.items)):
            self.hash_table[max(0, int(len(self.hash_table) * new_list[i]) - 1)].append(self.items[i])

    @staticmethod
    def post_process_bucket(bucket_list):
        bucket_list = [bucket_list[i] for i in range(len(bucket_list))]
        return bucket_list

    def compute(self):
        if len(self.items) > 0:
            self.bucket_items()
            sorted_list = []
            for i, bucket in enumerate(self.hash_table):
                sorter = InsertionSort(items=bucket, ascending=True)
                sorted_list.extend(self.post_process_bucket(sorter.sort()))
            return sorted_list
        else:
            return []


if __name__ == '__main__':
    items = [2, 5, 3, 0, 2, 3, 0, 3]
    bucket_sort = BucketSort(items=items)
    sorted_items = bucket_sort.compute()
    print(sorted_items)
