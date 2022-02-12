from linked_list import LinkedList
import math
import random

class DirectAddressTable:
    def __init__(self, items, m):
        self.items = items
        # creates an empty table where each entry is a doubly linked list and there are enough entries for the maximum value item
        self.table = [None] * m
        self.__build_table()

    #################################
    # HASH TABLE INITIAL CONSTRUCTION
    #################################
    def __build_table(self):
        for item in self.items:
            hash_value = self.compute_hash(item=str(item))
            if self.table[hash_value] is not None:
                self.table[hash_value].insert(key=item, current_node=self.table[hash_value].nil)
            else:
                self.table[hash_value] = LinkedList(items=[item])

    ###########################
    # HASH FUNCTION COMPUTATION
    ###########################
    @staticmethod
    def __find_radix(integer_list):
        base = len(integer_list)
        radix = sum([integer_list[i] ** (base - (i + 1)) for i in range(len(integer_list))])
        return radix

    def compute_hash(self, item, method='multiplication'):
        integer_list = [ord(x) for x in str(item)]
        k = self.__find_radix(integer_list)
        if method == 'division':
            return k % len(self.table)
        if method == 'multiplication':
            m, A = len(self.table), (math.sqrt(5) - 1) / 2
            fractional = math.sqrt((k * A))
            mod_frac = fractional % 1
            hash_value = math.floor(m * mod_frac)
            return hash_value

    ########################
    # HASH TABLE OPERATIONS
    ########################
    def search(self, key):
        hash_value = self.__compute_hash(x=key)
        return self.table[hash_value].search(k=key)

    def insert(self, x):
        hash_value = self.compute_hash(x)
        if self.table[hash_value] is not None:
            self.table[hash_value].insert(key=x, current_node=self.table[hash_value].nil)
        else:
            self.table[hash_value] = LinkedList(items=[x])

    def delete(self, key):
        hash_value = self.compute_hash(x=key)
        return self.table[hash_value].delete(k=key)


if __name__ == '__main__':
    items = [{str(random.randint(0, 100)): random.randint(0, 1000)} for i in range(1000)]
    table = DirectAddressTable(items=items, m=1000)
    print(table.table)

