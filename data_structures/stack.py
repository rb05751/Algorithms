class Stack:
    def __init__(self, init_items):
        self.init_items = init_items
        self.stack = [item for item in init_items]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop(-1)

    def __repr__(self):
        return str(self.stack)

if __name__ == '__main__':
    items = [2, 3, 6]
    stack = Stack(init_items=items)
    print(stack)
    stack.push(8)
    print(stack)
    stack.push(5)
    print(stack)
    stack.pop()
    print(stack)
