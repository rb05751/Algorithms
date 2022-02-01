class Node:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_sib = None
        self.parent = None


class Tree:
    def __init__(self, items, k):
        self.A = items
        self.k = k  # maximum number of children each node can have
        self.root = None
        self.__build_tree()

    def __build_tree(self):
        i = 0  # last left child key index
        j = 1  # last right sibling
        last_left = None
        done = False
        while j + 1 < len(self.A):
            if i == 0:
                root_node = Node(self.A[0])  # create root node
                self.root = root_node  # set root ptr
                root_node.left_child = Node(self.A[i + 1]) if len(self.A) > 1 else None  # create roots first left child
                root_node.left_child.parent = root_node if root_node.left_child is not None else None
                i += 1  # last left child is now marked in array
                last_left = root_node.left_child
                last_node = root_node.left_child
                for n in range(1, self.k):
                    try:
                        r_sib_node = Node(self.A[i + n])
                        last_node.right_sib = r_sib_node
                        r_sib_node.parent = root_node
                        last_node = r_sib_node
                        j += 1
                    except:
                        done = True
                        break
                if done:
                    break
            else:
                new_left_node = Node(self.A[j + 1])
                last_left.left_child = new_left_node
                new_left_node.parent = last_left
                last_node = new_left_node
                j += 1
                for n in range(1, self.k):
                    try:
                        r_sib_node = Node(self.A[j + 1])
                        r_sib_node.parent = last_left
                        last_node.right_sib = r_sib_node
                        last_node = r_sib_node
                        j += 1
                    except:
                        done = True
                        break
                if done:
                    break
                last_left = new_left_node

    def print_tree(self, node):
        if node is None:
            return
        else:
            print(node.key)
            self.print_tree(node=node.left_child)
            self.print_tree(node=node.right_sib)


if __name__ == '__main__':
    items = [7, 2, 1, 8, 6, 9, 4]
    tree = Tree(items=items, k=3)
    tree.print_tree(node=tree.root)
