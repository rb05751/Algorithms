from doubly_linked_list import LinkedList
import math
import random


class HashTable:
    def __init__(self, items, table_size, auxiliary_hash_method='universal', collision_resolution='chaining'):
        self.items = items
        self.collision_resolution = collision_resolution
        self.auxiliary_hash_method = auxiliary_hash_method
        # creates an empty table where each entry is a doubly linked list and there are enough entries for the maximum value item
        self.table = [None] * table_size
        self.hash_functions = {
            'division': self.__divide,
            'multiplication': self.__multiply,
            'universal': self.__universal
        }
        self.__build_table()

    #################################
    # HASH TABLE INITIAL CONSTRUCTION
    #################################
    def __build_table(self):
        for item in self.items:
            if self.collision_resolution == 'chaining':
                hash_value = self.__compute_hash(item=str(item))
                if self.table[hash_value] is not None:
                    self.table[hash_value].insert(key=item, current_node=self.table[hash_value].nil)
                else:
                    self.table[hash_value] = LinkedList(items=[item])
            else:
                hash_value = self.__probe(k=item, hash_method='multiplication')
                if hash_value is None: continue
                self.table[hash_value] = item

    ##############################
    # HASH FUNCTION COMPUTATIONS #
    ##############################
    def __probe(self, k, hash_method, i=0, inserting=True):
        hash_value = self.__compute_hash(item=k, method=hash_method, i=i)
        table_slot = self.table[hash_value]
        if not inserting and table_slot == k: return hash_value
        if table_slot in [None, 'DELETED'] and inserting:
            return hash_value
        elif (i + 1) % len(self.table) != 0: # if we are not where we started yet
            hash_value = self.__probe(k=k, hash_method=hash_method, i=i + 1, inserting=inserting)
        else:
            return None
        return hash_value

    def __divide(self, k):
        return k % len(self.table)

    def __universal(self, k):
        p = 999331
        return ((2*k + 5) % (p+1)) % len(self.table)

    def __multiply(self, k):
        m, A = len(self.table), (math.sqrt(5) - 1) / 2
        fractional = math.sqrt((k * A))
        mod_frac = fractional % 1
        hash_value = math.floor(m * mod_frac)
        return hash_value

    @staticmethod
    def __find_radix(integer_list):
        base = len(integer_list)
        radix = sum([integer_list[i] ** (base - (i + 1)) for i in range(len(integer_list))])
        return radix

    def __compute_hash(self, item, method='multiplication', i=0):
        integer_list = [ord(x) for x in str(item)]
        k = self.__find_radix(integer_list)
        if self.collision_resolution == 'chaining':
            return self.hash_functions[method](k)
        elif self.collision_resolution == 'linear probing':
                return (self.hash_functions[method](k) + (i % len(self.table))) % len(self.table)
        elif self.collision_resolution == 'quadratic probing':
                c1, c2 = 1, 3
                return (self.hash_functions[method](k) + c1 * (i % len(self.table)) + c2 * ((i % len(self.table)) ** 2)) % len(self.table)
        elif self.collision_resolution == 'double hashing':
                return (self.hash_functions[method](k) + (i % len(self.table)) * self.__divide(k=k)) % len(self.table)

    #########################
    # HASH TABLE OPERATIONS #
    #########################
    def search(self, key):
        if self.collision_resolution == 'chaining':
            hash_value = self.__compute_hash(item=key)
            return self.table[hash_value].search(k=key)
        else:
            hash_value = self.__probe(k=key, hash_method='multiplication', inserting=False)
            if hash_value is None: raise Exception(f"Item does not exist in this table")
            return hash_value

    def insert(self, x):
        hash_value = self.__compute_hash(x)
        if self.collision_resolution == 'chaining':
            if self.table[hash_value] is not None:
                self.table[hash_value].insert(key=x, current_node=self.table[hash_value].nil)
            else:
                self.table[hash_value] = LinkedList(items=[x])
        else:
            hash_value = self.__probe(k=x, hash_method=self.auxiliary_hash_method)
            if hash_value is None: raise Exception(f"Cannot insert item because table is full.")
            self.table[hash_value] = x

    def delete(self, key):
        if self.collision_resolution == 'chaining':
            hash_value = self.__compute_hash(item=key)
            return self.table[hash_value].delete(k=key)
        else:
            hash_value = self.__probe(k=key, hash_method=self.auxiliary_hash_method, i=0, inserting=False)
            if hash_value is None: raise Exception("Item is not in table")
            self.table[hash_value] = "DELETED"
            return hash_value


if __name__ == '__main__':
    items = [{'54': 1000}, {'99': 983}, {'44': 962}, {'59': 767}, {'25': 355}, {'67': 668}, {'74': 696}, {'74': 320}, {'74': 867}, {'74': 188}, {'74': 120}]
    table = HashTable(items=items, auxiliary_hash_method='universal', collision_resolution='linear probing', table_size=1000)
    print(table.table)
    table.insert(x={'54': 1000})
    table.insert(x={'54': 1000})
    table.insert(x={'54': 1000})
    table.insert(x={'54': 1000})
    print(table.table)
    table.delete(key={'54': 1000})
    print(table.table)
    table.delete(key={'54': 1000})
    print(table.table)
    print(table.search(key={'74': 867}))



