import sys

from linked_list import LinkedList


class DirectAddressTable:
    def __init__(self, items):
        self.items = items
        # creates an empty table where each entry is a doubly linked list and there are enough entries for the maximum value item
        self.table = [None] * max(items)*2
        self.__build_table()

    def __build_table(self):
        for item in self.items:
            if self.table[item] is not None:
                self.table[item].insert(key=item, current_node=self.table[item].nil)
            else:
                self.table[item] = LinkedList(items=[item])

    def search(self, key):
        return self.table[key].search(k=key)

    def insert(self, x):
        hash_value = hash(str(x))
        hash_value = int(((hash_value + sys.maxsize) / (sys.maxsize + sys.maxsize)) * len(self.table))
        self.table[hash_value].insert(key=x, current_node=self.table[hash_value].nil)

    def delete(self, key):
        return self.table[key].delete(k=key)



if __name__ == '__main__':
    table = DirectAddressTable(items=list(range(1000)) + list(range(100)) + list(range(5000)))
    table = table.table



