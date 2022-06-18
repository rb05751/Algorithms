class Queue:
    def __init__(self, init_items, n):
        self.init_items = init_items
        self.queue = [''] * n
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        if (self.head == self.tail + 1) or (self.head == 0 and self.tail == len(self.queue)):
            raise Exception("Overflow!")
        self.queue[self.tail] = item
        if self.tail == len(self.queue):
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.head == self.tail:
            raise Exception("Underflow!")
        item = self.queue[self.head]
        if self.head == len(self.queue):
            self.head = 0
        else:
            self.head += 1
        return item

    def __repr__(self):
        return str(self.queue)

if __name__ == '__main__':
    queue = Queue(init_items=[2, 4], n=30)
    print(queue)
    queue.enqueue(item=3)
    print(queue)
    print(queue.tail)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)