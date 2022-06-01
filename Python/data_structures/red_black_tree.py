"""Self-balancing Binary Search Tree where each node consists of a color attribute that is either red or black.
The tree at all times must satisfy the following properties:

1. Every node is either red or black.
2. The root is black.
3. Every leaf (NIL) is black.
4. If a node is red, then both of its children are black.
5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.
"""

from binary_search_tree import BinarySearchTree, Node


class RBNode(Node):
    def __init__(self, key, color, parent=None, left_child=None, right_child=None):
        super().__init__(key, parent, left_child, right_child)
        self.color = color
        self.__build_sentinels()

    def __build_sentinels(self):
        if self.key is not None:
            self.left_child = RBNode(key=None, color='Black', parent=self)
            self.right_child = RBNode(key=None, color='Black', parent=self)


class RedBlackTree(BinarySearchTree):
    def __init__(self, init_items):
        self.init_items = init_items
        self.root = None
        self.__build(init_items)

    ##################
    # HELPER METHODS #
    ##################
    def __rb_transplant(self, node1, node2):
        """Transplants subtree rooted at node1 with node2's subtree"""
        if node1.parent is None:
            self.root = node2
        elif node1 is node1.parent.left_child:
            node1.parent.left_child = node2
        else:
            node1.parent.right_child = node2

        node2.parent = node1.parent

    def left_rotate(self, node):
        """Makes the current nodes right child its parent while the current node takes over
         parental guidance of its right child's left subtree"""
        y = node.right_child
        node.right_child = y.left_child
        if y.left_child.key is not None:
            y.left_child.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node is node.parent.left_child:
            node.parent.left_child = y
        else:
            node.parent.right_child = y
        y.left_child = node
        node.parent = y

    def right_rotate(self, node):
        """Makes the current nodes left child its parent while the current node takes over
         parental guidance of its left child's right subtree"""
        y = node.left_child
        node.left_child = y.right_child
        if y.right_child.key is not None:
            y.right_child.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node is node.parent.left_child:
            node.parent.left_child = y
        else:
            node.parent.right_child = y
        y.right_child = node
        node.parent = y

    def __build(self, init_items):
        for item in init_items:
            self.__insert(key=item, current_node=self.root)

    def __insert_fixup(self, current_node):
        if current_node.parent is None:
            self.root.color = 'Black'
        elif current_node.parent.color == 'Black':
            self.root.color = 'Black'
        else:
            if current_node.parent is current_node.parent.parent.left_child:
                current_nodes_uncle = current_node.parent.parent.right_child
                # CASE 1
                if current_nodes_uncle.color == 'Red':
                    current_node.parent.color = 'Black'
                    current_nodes_uncle.color = 'Black'
                    current_node.parent.parent.color = 'Red'
                    return self.__insert_fixup(current_node=current_node.parent.parent)
                # CASE 2
                elif current_node is current_node.parent.right_child:
                    current_node = current_node.parent
                    self.left_rotate(node=current_node)
                # CASE 3
                current_node.parent.color = 'Black'
                current_node.parent.parent.color = 'Red'
                self.right_rotate(node=current_node.parent.parent)
                return self.__insert_fixup(current_node=current_node)
            else:
                current_nodes_uncle = current_node.parent.parent.left_child
                # CASE 1
                if current_nodes_uncle.color == 'Red':
                    current_node.parent.color = 'Black'
                    current_nodes_uncle.color = 'Black'
                    current_node.parent.parent.color = 'Red'
                    return self.__insert_fixup(current_node=current_node.parent.parent)
                # CASE 2
                elif current_node is current_node.parent.left_child:
                    current_node = current_node.parent
                    self.right_rotate(node=current_node)
                # CASE 3
                current_node.parent.color = 'Black'
                current_node.parent.parent.color = 'Red'
                self.left_rotate(node=current_node.parent.parent)
                return self.__insert_fixup(current_node=current_node)

        self.root.color = 'Black'

    def __delete_fixup(self, current_node):
        if current_node is self.root or current_node.color == 'Red':
            current_node.color = 'Black'
            return

        if current_node is current_node.parent.left_child:
            current_nodes_sibling = current_node.parent.right_child
            if current_nodes_sibling.color == 'Red':
                current_nodes_sibling.color = 'Black'
                current_node.parent.color = 'Red'
                self.left_rotate(current_node.parent)
                current_nodes_sibling = current_node.parent.right_child
            if current_nodes_sibling.left_child.color == current_nodes_sibling.right_child.color == 'Black':
                current_nodes_sibling.color = 'Red'
                return self.__delete_fixup(current_node=current_node.parent)
            elif current_nodes_sibling.right_child.color == 'Black':
                current_nodes_sibling.left_child.color = 'Black'
                current_nodes_sibling.color = 'Red'
                self.right_rotate(node=current_nodes_sibling)
                current_nodes_sibling = current_nodes_sibling.parent.right_child
            current_nodes_sibling.color, current_node.parent.color, current_nodes_sibling.right_child.color = current_node.parent.color, 'Black', 'Black'
            self.left_rotate(node=current_node.parent)
            current_node = self.root
            return self.__delete_fixup(current_node=current_node)
        else:
            current_nodes_sibling = current_node.parent.left_child
            if current_nodes_sibling.color == 'Red':
                current_nodes_sibling.color = 'Black'
                current_node.parent.color = 'Red'
                self.right_rotate(current_node.parent)
                current_nodes_sibling = current_node.parent.left_child
            if current_nodes_sibling.left_child.color == current_nodes_sibling.right_child.color == 'Black':
                current_nodes_sibling.color = 'Red'
                return self.__delete_fixup(current_node=current_node.parent)
            elif current_nodes_sibling.left_child.color == 'Black':
                current_nodes_sibling.right_child.color = 'Black'
                current_nodes_sibling.color = 'Red'
                self.left_rotate(node=current_nodes_sibling)
                current_nodes_sibling = current_nodes_sibling.parent.left_child
            current_nodes_sibling.color, current_node.parent.color, current_nodes_sibling.left_child.color = current_node.parent.color, 'Black', 'Black'
            self.right_rotate(node=current_node.parent)
            current_node = self.root
            return self.__delete_fixup(current_node=current_node)

    ###################
    # MAIN OPERATIONS #
    ###################
    def __insert(self, key=None, current_node=None):
        if current_node is None:
            self.root = RBNode(key=key, color='Red')
            self.__insert_fixup(self.root)
        elif current_node.key is None:
            self.root = RBNode(key=key, color='Red')
            self.__insert_fixup(self.root)
        else:
            if key < current_node.key:
                if current_node.left_child.key is not None:
                    self.insert(key, current_node=current_node.left_child)
                else:
                    new_node = RBNode(key=key, color='Red', parent=current_node)
                    current_node.left_child.parent, current_node.left_child = None, new_node
                    self.__insert_fixup(current_node=new_node)
            else:
                if current_node.right_child.key is not None:
                    self.insert(key, current_node=current_node.right_child)
                else:
                    new_node = RBNode(key=key, color='Red', parent=current_node)
                    current_node.right_child.parent, current_node.right_child = None, new_node
                    self.__insert_fixup(current_node=new_node)

    def delete(self, key):
        node_to_delete = self.find(key=key, current_node=self.root)
        y, y_og_color = node_to_delete, node_to_delete.color

        if node_to_delete.left_child.key is None:
            x = node_to_delete.right_child
            self.__rb_transplant(node_to_delete, x)
        elif node_to_delete.right_child.key is None:
            x = node_to_delete.left_child
            self.__rb_transplant(node_to_delete, x)
        else:
            y = self.find_minimum(node=node_to_delete.right_child)
            y_og_color = y.color
            x = y.right_child
            if y.parent is node_to_delete:
                x.parent = y
            else:
                self.__rb_transplant(node1=y, node2=y.right_child)
                y.right_child = node_to_delete.right_child
                y.right_child.parent = y
            self.__rb_transplant(node1=y, node2=y.right_child)
            y.left_child, y.left_child.parent, y.color = node_to_delete.left_child, y, node_to_delete.color

        if y_og_color == 'Black':
            self.__delete_fixup(current_node=x)


if __name__ == '__main__':
    tree = RedBlackTree(init_items=[41, 38, 31, 12, 19, 8])

    items_to_delete = [8, 12, 19, 31, 38, 41]

    for item in items_to_delete:
        tree.delete(item)

    print("Done")
