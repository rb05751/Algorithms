"""
Treap: A type of binary search tree where each node maintains both a key & a randomly assigned priority attribute.
The tree is structured such that the binary search property holds on the keys and the min heap property holds on the priorities.

Cool Fact: The resulting tree that satisfies the Treap properties is the same Binary Search Tree that would have been formed if
the nodes were inserted in order of their randomly assigned priorities into a regular Binary Search Tree.
"""

from binary_search_tree import Node
from red_black_tree import RedBlackTree
import random


class TreapNode(Node):
    def __init__(self, key, parent=None, left_child=None, right_child=None):
        super().__init__(key, parent, left_child, right_child)
        if key is not None:
            self.priority = random.randint(0, 1000000)
            self.left_child = TreapNode(key=None, parent=self)
            self.right_child = TreapNode(key=None, parent=self)


class Treap(RedBlackTree):
    def __init__(self, init_items):
        self.items = init_items
        self.root = None
        self.__build()

    def __build(self):
        for item in self.items:
            inserted_node = self.insert(key=item, current_node=self.root, node=TreapNode)
            self.__insert_fixup(current_node=inserted_node)

    def __insert_fixup(self, current_node):
        if current_node.parent is None: return

        if current_node.priority >= current_node.parent.priority:
            return
        else:
            if current_node.parent.right_child is current_node:
                self.left_rotate(node=current_node.parent)
            else:
                self.right_rotate(node=current_node.parent)
            return self.__insert_fixup(current_node=current_node)

    def delete(self, key):
        node_to_delete = self.find(key=key, current_node=self.root)
        if node_to_delete is None:
            raise Exception(f"Node with key = {key} does not exist in tree")
        else:
            if node_to_delete.right_child.key is not None:
                self.transplant(node1=node_to_delete, node2=node_to_delete.right_child)
            else:
                self.transplant(node1=node_to_delete, node2=node_to_delete.left_child)


if __name__ == '__main__':
    treap = Treap(init_items=[41, 38, 31, 12, 19, 8])

    items_to_delete = [8, 12, 19, 31, 38, 41]
    for item in items_to_delete:
        treap.delete(item)

    print("Done")
