"""
An Order Statistic Tree is an instance of a Red Black Tree that utilizes an extra node attribute 'size'
, which defines the number of nodes in a nodes subtree, to calculate the ith order statistic of any node
in the tree.
"""

from red_black_tree import RedBlackTree, RBNode


class OSNode(RBNode):
    def __init__(self, key, color, parent=None, left_child=None, right_child=None):
        super().__init__(key, color, parent, left_child, right_child)
        self.size = 1 if key is not None else 0  # all nodes when first created have size = 1 except the sentinels
        self.__build_sentinels()

    def __build_sentinels(self):
        if self.key is not None:
            self.left_child = OSNode(key=None, color='Black', parent=self)
            self.right_child = OSNode(key=None, color='Black', parent=self)


class OrderStatisticTree(RedBlackTree):
    def __init__(self, init_items):
        self.root = None
        self.__os_build(init_items)

    def __os_build(self, init_items):
        for item in init_items:
            self.__os_insert(key=item, current_node=self.root)

    def left_rotate(self, node):
        x, y = super().left_rotate(node)
        y.size = x.size
        x.size = x.left_child.size + x.right_child.size + 1

    def right_rotate(self, node):
        x, y = super().right_rotate(node)
        y.size = x.size
        x.size = x.left_child.size + x.right_child.size + 1

    def __os_insert(self, key=None, current_node=None):
        if current_node is None:
            self.root = OSNode(key=key, color='Red')
            self.insert_fixup(self.root)
        else:
            if key < current_node.key:
                if current_node.left_child.key is not None:
                    current_node.size += 1  # increment size attribute
                    self.__os_insert(key, current_node=current_node.left_child)
                else:
                    new_node = OSNode(key=key, color='Red', parent=current_node)
                    current_node.size += 1  # increment size attribute
                    current_node.left_child.parent, current_node.left_child = None, new_node
                    self.insert_fixup(current_node=new_node)
            else:
                if current_node.right_child.key is not None:
                    current_node.size += 1  # increment size attribute
                    self.__os_insert(key, current_node=current_node.right_child)
                else:
                    new_node = OSNode(key=key, color='Red', parent=current_node)
                    current_node.size += 1  # increment size attribute
                    current_node.right_child.parent, current_node.right_child = None, new_node
                    self.insert_fixup(current_node=new_node)

    def os_delete_fixup(self, node):
        if node is not None:
            node.size -= 1
            return self.os_delete_fixup(node.parent)
        else:
            return

    def delete(self, key):
        node_to_delete = self.find(key=key, current_node=self.root)
        y, y_og_color = node_to_delete, node_to_delete.color

        if node_to_delete.left_child.key is None:
            x = node_to_delete.right_child
            self.rb_transplant(node_to_delete, x)
        elif node_to_delete.right_child.key is None:
            x = node_to_delete.left_child
            self.rb_transplant(node_to_delete, x)
        else:
            y = self.find_minimum(node=node_to_delete.right_child)
            y_og_color = y.color
            x = y.right_child
            if y.parent is node_to_delete:
                x.parent = y
            else:
                self.rb_transplant(node1=y, node2=y.right_child)
                y.right_child = node_to_delete.right_child
                y.right_child.parent = y
            self.rb_transplant(node1=y, node2=y.right_child)
            y.left_child, y.left_child.parent, y.color = node_to_delete.left_child, y, node_to_delete.color

        self.os_delete_fixup(node=x.parent)
        if y_og_color == 'Black':
            super().delete_fixup(current_node=x)


if __name__ == '__main__':
    os_tree = OrderStatisticTree(init_items=[41, 38, 31, 12, 19, 8])

    items_to_delete = [8, 12, 19, 31, 38, 41]

    for item in items_to_delete:
        os_tree.delete(item)

    print("Done")
