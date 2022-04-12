from sorting.quick_sort import QuickSort


class Node:
    def __init__(self, key, parent=None, left_child=None, right_child=None):
        self.key = key
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


class BinarySearchTree:
    def __init__(self, init_items, randomized):
        self.root = None
        self.partitioner = QuickSort(items=[], is_random=randomized)
        self.__build(items=init_items)

    ###################
    # PRIVATE METHODS #
    ###################
    def __build(self, items, parent=None):
        """partitions the initial items recursively while inserting each partitioned node into tree"""
        if len(items) == 0:
            return Node(key=None, left_child=None, right_child=None, parent=parent)
        if len(items) == 1:
            return Node(key=items[0], left_child=Node(key=None), right_child=Node(key=None), parent=parent)
        else:
            _, partition_idx = self.partitioner.reg_partition(A=items)
            new_node = Node(key=items[partition_idx])
            if parent is not None:
                new_node.parent = parent
            else:
                self.root = new_node

            # recurse
            new_node.left_child = self.__build(items[:partition_idx], parent=new_node)
            new_node.right_child = self.__build(items[partition_idx + 1:], parent=new_node)
        return new_node

    def __find_minimum(self, node):
        if node.left_child.key is None:
            return node
        else:
            return self.__find_minimum(node=node.left_child)

    def __find_maximum(self, node):
        if node.right_child.key is None:
            return node
        else:
            return self.__find_maximum(node=node.right_child)

    def __find_successor(self, node):
        if node.right_child.key is not None:
            return self.__find_minimum(node=node.right_child)

        trailing_node = node.parent
        while trailing_node.key is not None and node is trailing_node.right:
            node = trailing_node
            trailing_node = trailing_node.parent
        return trailing_node

    def __find_predecessor(self, node):
        if node.left_child.key is not None:
            return self.__find_maximum(node=node.left_child)

        trailing_node = node.parent
        while trailing_node.key is not None and node is trailing_node.left:
            node = trailing_node
            trailing_node = trailing_node.parent
        return trailing_node

    def __transplant(self, node1, node2):
        """Transplants subtree rooted at node1 with node2's subtree"""
        if node1.parent.key is None:
            self.root = node2
        elif node1 is node1.parent.left_child:
            node1.parent.left_child = node2
        else:
            node1.parent.right_child = node2

        if node2.key is not None:
            node2.parent = node1.parent

    def __print_tree(self, node):
        print(f"Node: {node.key}")
        if node.left_child is not None:
            print(f"Node: {node.key} Left child: {node.left_child.key}")
            self.__print_tree(node.left_child)
        if node.right_child is not None:
            print(f"Node: {node.key} Right child: {node.right_child.key}")
            self.__print_tree(node.right_child)

    ##################
    # PUBLIC METHODS #
    ##################

    def insert(self, key=None, current_node=None):
        if self.root is None: # if tree is empty
            self.root = Node(key)
            return
        if current_node is None: current_node = self.root # init starting position for all inserts

        if current_node.key is not None:
            if key < current_node.key:
                self.insert(key=key, current_node=current_node.left_child)
            else:
                self.insert(key=key, current_node=current_node.right_child)
        else:
            if current_node.parent.left_child is current_node:
                new_node = Node(key=key, parent=current_node.parent)
                current_node.parent.left_child = new_node
                new_node.parent = current_node.parent
            else:
                new_node = Node(key=key, parent=current_node.parent)
                current_node.parent.right_child = new_node
                new_node.parent = current_node.parent

    def find(self, key=None, current_node=None):
        if self.root is None: # if tree is empty
            return None
        if current_node is None: current_node = self.root # init starting position for all inserts

        if current_node.key is None:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self.find(key=key, current_node=current_node.left_child)
        else:
            return self.find(key=key, current_node=current_node.right_child)

    def delete(self, key):
        node = self.find(key=key)
        if node is None:
            raise Exception(f"Node with key = {key} does not exist in tree")
        if node.left_child.key == node.right_child.key == None:
            if node is self.root:
                self.root = Node(key=None)
                return
            if node.parent.left_child is node: node.parent.left_child = Node(key=None)
            if node.parent.right_child is node: node.parent.right_child = Node(key=None)

        elif node.left_child.key is None and node.right_child.key is not None:
            self.__transplant(node1=node, node2=node.right_child)
        elif node.right_child.key is None and node.left_child.key is not None:
            self.__transplant(node1=node, node2=node.left_child)
        elif node.left_child.key is not None and node.right_child.key is not None:
            successor = self.__find_successor(node=node)
            if successor is node.right_child:
                self.__transplant(node1=node, node2=successor)
                successor.left_child = node.left_child
                successor.left_child.parent = successor
            else:
                self.delete(key=successor.key) # I <3 Recursion :)
                if node is self.root: self.root = successor
                successor.left_child, successor.left_child.parent = node.left_child, successor
                successor.right_child, successor.right_child.parent = node.right_child, successor
                successor.parent = node.parent
                if node.parent is None: return
                if node.parent.left_child is node: successor.parent.left_child = successor
                if node.parent.right_child is node: successor.parent.right_child = successor

    def __repr__(self):
        self.__print_tree(node=self.root)
        return ""


if __name__ == '__main__':
    bst = BinarySearchTree(init_items=[12, 5, 2, 9, 18, 15, 19, 17, 13], randomized=True)
    print(bst)
    print("Deleting key 13")
    bst.delete(key=13)
    print(f"----New Tree----")
    print(bst)
