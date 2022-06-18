from doubly_linked_list import Node, DoublyLinkedList


class CircularDoublyLinkedList(DoublyLinkedList):
    def __init__(self, init_items, sorted=False):
        self.nil = Node(data=None)  # This is our sentinel
        self.init_items = init_items
        self.sorted = sorted
        self.build()

    def build(self):
        if len(self.init_items) == 0:
            return "No items to build list from"
        self.nil.next = Node(self.init_items[-1])
        self.nil.prev = self.nil.next
        self.nil.next.prev = self.nil
        self.nil.next.next = self.nil
        self.init_items = self.init_items[:-1]
        for _ in range(len(self.init_items)):
            self.insert(key=self.init_items.pop(), current_node=self.nil)

    def delete(self, k):
        x = self.search(k=k)
        if x.data is not None:
            if x.next.data is None:
                x.prev.next = x.next
                x.prev, x.next = None, None
            else:
                x.prev.next = x.next
                x.next.prev = x.prev
                x.next, x.prev = None, None
        else:
            return f"Item with key {k} does not exist"
        return x

    def __repr__(self):
        full_list = []
        x = self.nil
        while x.next.data is not None:
            full_list.append(x.next.data)
            x = x.next

        return str(full_list)


if __name__ == '__main__':
    circular_list = CircularDoublyLinkedList(init_items=[3, 6, 2, 7, 5, 1, 4])
    print(circular_list)

    items_to_delete = [4, 5, 1, 3, 2, 7, 6]

    for item in items_to_delete:
        circular_list.delete(k=item)
        print(circular_list)