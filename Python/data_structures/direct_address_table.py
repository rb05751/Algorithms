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

    def insert(self, key):
        self.table[key].insert(key=key, current_node=self.table[key].nil)

    def delete(self, key):
        return self.table[key].delete(k=key)



if __name__ == '__main__':
    table = DirectAddressTable(items=list(range(100)) + list(range(10)) + list(range(500)))
    print(table.table)


