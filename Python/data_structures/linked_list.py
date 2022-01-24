import numpy as np

"""Object-oriented approach to Linked-list"""


class Node:
    def __init__(self, data):
        self.key = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.nil = Node(data=None)  # This is our sentinel

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

    def search(self, k):
        x = self.nil
        while x.next is not None or x.key != k:
            x = x.next
        return x

    def delete(self, k):
        x = self.search(k=k)
        if x.key is not None:
            if x.next is None:
                x.prev.next = x.next
            else:
                x.prev.next = x.next
                x.next.prev = x.prev
        else:
            return f"Item with key {k} does not exist"

    def __repr__(self):
        full_list = []
        x = self.nil
        while x.next is not None:
            full_list.append(x.next.key)
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

    def insert(self, key):
        if self.free == 'nan':
            raise Exception("There is no more space left in the list")
        else:
            x = self.free
            if self.free + 1 == self.A.shape[1]:
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

    def __repr__(self):
        return str(self.A)


if __name__ == '__main__':
    """Regular Linked List implementation"""
    # L = LinkedList()
    # L.add_node(data=1)
    # L.add_node(data=4)
    # L.add_node(data=16)
    # L.add_node(data=9)
    # print(L)
    # L.add_node(data=25)
    # print(L)
    # L.delete(k=1)
    # print(L)

    """Linked List Implementation with Array"""
    L = LinkedArrayList(M=10)
    items = [23, 17, 4, 6, 8, 19]
    for item in items:
        L.insert(item)
        print(f"Insert {item}")
        print(f"Head: {L.L}")
        print(f"Free: {L.free}")
        print(L.A)

    print(f"Deleting index 5")
    L.delete(index=5)
    print(f"Head: {L.L}")
    print(f"Free: {L.free}")
    print(L.A)

