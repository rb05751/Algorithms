import numpy as np
import random

"""Object-oriented approach to Linked-list"""


class Node:
    def __init__(self, data):
        self.data = data # satellite data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, items, sorted=False):
        self.nil = Node(data=None)  # This is our sentinel
        self.items = items
        self.sorted = sorted
        self.__build()

    def add_node(self, data):
        if self.nil.next is None:
            node = Node(data=data)
            node.next = self.nil.next
            node.prev = self.nil
            self.nil.next = node
        else:
            node = Node(data=data)
            node.next = self.nil.next
            node.prev = self.nil
            node.next.prev = node
            self.nil.next = node

    def insert(self, key, current_node):
        if self.sorted:
            if current_node.next is None:
                node = Node(key)
                current_node.next = node
                node.prev = current_node
                return
            elif current_node.next.data > key:
                node = Node(key)
                current_node.next.prev = node
                node.prev = current_node
                node.next = current_node.next
                current_node.next = node
                return
            else:
                self.insert(key, current_node=current_node.next)
        else:  # then we are passing in the sentinel
            node = Node(key)
            node.next = current_node.next
            if current_node.next is not None:
                current_node.next.prev = node
                current_node.next = node
                node.prev = current_node
                return
            else:
                current_node.next = node
                node.prev = current_node
                return

    def __build(self):
        if len(self.items) == 0:
            return "No items to build list from"
        self.nil.next = Node(self.items[0])
        self.nil.next.prev = self.nil
        for item in self.items[1:]:
            self.insert(key=item, current_node=self.nil)

    def search(self, k):
        x = self.nil
        while x.next is not None and x.data != k:
            x = x.next
        return x

    def get_min(self, L_nil, extract=False):
        if L_nil.next is None:
            return None
        if self.sorted:
            if extract:
                min_item = L_nil.next
                L_nil.next = min_item.next
                if min_item.next is not None:
                    min_item.next.prev = L_nil
                return min_item
            else:
                if L_nil.next is not None:
                    return L_nil.next.key
                else:
                    return None

    def union(self, L_2, L_3=None): # merges subject list with another list
        L_3 = DoublyLinkedList(items=[]) if L_3 is None else L_3
        min_item_1 = self.get_min(L_nil=self.nil, extract=False)
        min_item_2 = self.get_min(L_nil=L_2.nil, extract=False)
        if min_item_1 is not None and min_item_2 is not None:
            if min_item_1 <= min_item_2:
                min_item = self.get_min(L_nil=self.nil, extract=True)
            else:
                min_item = self.get_min(L_nil=L_2.nil, extract=True)
            self.insert(key=min_item.key, current_node=L_3.nil)
            self.union(L_2, L_3)
        elif min_item_1 is None and min_item_2 is not None:
            min_item = self.get_min(L_nil=L_2.nil, extract=True)
            self.insert(key=min_item.key, current_node=L_3.nil)
            self.union(L_2, L_3)
        elif min_item_1 is not None and min_item_2 is None:
            min_item = self.get_min(L_nil=self.nil, extract=True)
            self.insert(key=min_item.key, current_node=L_3.nil)
            self.union(L_2, L_3)
        else: # this means we have inserted all elements from each list into L_3
            return L_3
        return L_3

    def delete(self, k):
        x = self.search(k=k)
        if x.data is not None:
            if x.next is None:
                x.prev.next = x.next
                x.prev = None
            else:
                x.prev.next = x.next
                x.next.prev = x.prev
        else:
            return f"Item with key {k} does not exist"
        return x

    def __len__(self):
        full_list = []
        x = self.nil
        while x.next is not None:
            full_list.append(x.next.data)
            x = x.next

        return len(full_list)

    def __repr__(self):
        full_list = []
        x = self.nil
        while x.next is not None:
            full_list.append(x.next.data)
            x = x.next

        return str(full_list)


"""Non OOP Pointers are indices in an array and List is stored in multi-dimensional array"""
"""Goal is to implement a compact multi-dim array rep of linked list"""


class LinkedArrayList:
    def __init__(self, M):
        self.L = 'nan'
        self.free = 0
        self.A = np.zeros(shape=(3, M))
        self.__init_array()

    def __init_array(self):
        for i in range(self.A.shape[1]):
            self.A[:, i] = np.array(['nan' for _ in range(self.A.shape[0])])

    def __restore_position(self, item_idx):
        if self.A[2, item_idx] != 'nan':
            if self.A[1, item_idx] < self.A[1, item_idx-1]: # if this item is greater than last one
                # swap
                tmp = self.A[1, item_idx-1]
                self.A[1, item_idx-1] = self.A[1, item_idx]
                self.A[1, item_idx] = tmp
                self.__restore_position(item_idx=item_idx-1)
            else:
                return
        else:
            return

    def insert(self, key):
        if self.free == 'nan':
            raise Exception("There is no more space left in the list")
        else:
            x = self.free
            if self.free + 1 == self.A.shape[1]: # we've hit end of list
                self.free = 'nan'
            else:
                self.free += 1

            # insert object in position
            self.A[0, x] = 'nan'  # points to next object
            self.A[1, x] = key
            if self.L == 'nan':
                self.A[2, x] = 'nan'
                self.L = x
            else:
                self.A[2, x] = x - 1  # reference last object
                self.A[0, x - 1] = x  # change prev objects next ptr to this ones

            self.__restore_position(item_idx=x)

    def delete(self, index):
        if self.L == 'nan':
            raise Exception("Cannot delete from empty list")
        """Takes in an index from which all items > index need to be shifted to index"""
        if index == self.A.shape[1] - 1:  # if we delete the last item in the list
            self.A[:, index] = np.array(['nan', 'nan', 'nan'])
            self.A[0, index - 1] = 'nan'
            self.free = index
        elif index == 0:  # if we delete the first item in the list
            for i in range(self.A.shape[1] - 1):
                self.A[:, i] = self.A[:, i + 1]
                if i == 0:
                    self.A[2, 0] = 'nan'  # set first prev ptr to 'nan'
                    self.A[0, 0] = index + 1
                    continue
                else:
                    self.A[0, i] = self.A[0, i] - 1 if self.A[0, i] != 'nan' else 'nan'
                    self.A[2, i] -= 1 if self.A[2, i] != 'nan' else 'nan'
        else:
            for i in range(index, self.A.shape[1] - 1):
                self.A[:, i] = self.A[:, i + 1]
                if self.A[0, i] == 'nan':
                    self.free = i + 1
                self.A[0, i] = self.A[0, i] - 1 if self.A[0, i] != 'nan' else 'nan'
                self.A[2, i] -= 1 if self.A[2, i] != 'nan' else 'nan'

    def search(self, i, k):
        if i != 'nan' and self.A[1, i] < k:
            j = random.randint(0,self.free-1)
            if self.A[1, i] < self.A[1, j] <= k:
                i = j
                if self.A[1, j] == k:
                    return i
            return self.search(i=i+1, k=k) # keep searching starting at next index
        if i == 'nan':
            return None
        if self.A[1, i] > k:
            return None
        else:
            return i

    def __repr__(self):
        return str(self.A)


if __name__ == '__main__':
    import random
    import sys
    sys.setrecursionlimit(10**6)

    items = list(range(50))
    random.shuffle(items)
    linked_list = LinkedArrayList(M=len(items)*2)

    for item in items:
        linked_list.insert(key=item)

    linked_list.delete(index=31)
    print(linked_list)

    print(linked_list.search(i=linked_list.L, k=49))
