

class Node:
    def __init__(self, data):
        self.key = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.nil = Node(data=None) # This is our sentinel

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

if __name__ == '__main__':
    L = LinkedList()
    L.add_node(data=1)
    L.add_node(data=4)
    L.add_node(data=16)
    L.add_node(data=9)
    print(L)
    L.add_node(data=25)
    print(L)
    L.delete(k=1)
    print(L)





