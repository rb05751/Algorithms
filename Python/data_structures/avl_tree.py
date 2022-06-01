"""
An AVL Tree is a self-balancing binary search tree that through maintaining the invariant
that the heights of each nodes children only differ by at most one, can maintain an overall height of O(lgn).
"""
from binary_search_tree import Node
from red_black_tree import RedBlackTree


class AVLNode(Node):
    def __init__(self, key, parent=None, left_child=None, right_child=None):
        super().__init__(key, parent, left_child, right_child)
        self.height = None
        self.max_height_child = None
        self.__build_sentinels()
        self.set_height()

    def find_max_height_child(self):
        if self.key is None: return
        if self.left_child.key is None and self.right_child.key is None: return
        elif self.left_child.key is not None and self.right_child.key is None:
            self.max_height_child = self.left_child
        elif self.left_child.key is None and self.right_child.key is not None:
            self.max_height_child = self.right_child
        else:
            if self.left_child.height <= self.right_child.height:
                self.max_height_child = self.right_child
            else:
                self.max_height_child = self.left_child

    def set_height(self):
        if self.key is None: return
        if self.left_child.key is None and self.right_child.key is None:
            self.height = 0
        elif self.left_child.key is not None and self.right_child.key is None:
            self.height = self.left_child.height + 1
        elif self.left_child.key is None and self.right_child.key is not None:
            self.height = self.right_child.height + 1
        else:
            self.height = max([self.right_child.height, self.left_child.height]) + 1

        self.find_max_height_child()

    def __build_sentinels(self):
        if self.key is not None:
            self.left_child = AVLNode(key=None, parent=self)
            self.right_child = AVLNode(key=None, parent=self)


class AVLTree(RedBlackTree):
    def __init__(self, init_items):
        self.items = init_items
        self.root = None
        self.__avl_build()

    ##################
    # HELPER METHODS #
    ##################
    def __avl_build(self):
        for item in self.items:
            inserted_node = self.insert(key=item, current_node=self.root, node=AVLNode)
            self.__update_heights(current_node=self.root)
            self.__balance(current_node=inserted_node, path_up_tree=[])

    def __update_heights(self, current_node):
        if current_node.left_child is None and current_node.right_child is None:
            return current_node
        else:
            if current_node.left_child is not None:
                self.__update_heights(current_node=current_node.left_child)
            if current_node.right_child is not None:
                self.__update_heights(current_node=current_node.right_child)

        current_node.set_height()
        return current_node

    @staticmethod
    def __check_balance_factor(current_node):
        if current_node.left_child.key is not None and current_node.right_child.key is not None:
            return abs(current_node.left_child.height - current_node.right_child.height)
        elif current_node.left_child.key is None and current_node.right_child.key is not None:
            return current_node.right_child.height
        else:
            return current_node.left_child.height

    def __balance(self, current_node, path_up_tree):
        if current_node is None: return
        if current_node.height == 0:
            path_up_tree.append(current_node)
            return self.__balance(current_node.parent, path_up_tree)
        balance_factor = self.__check_balance_factor(current_node)
        if balance_factor < 2:
            path_up_tree.append(current_node)
            return self.__balance(current_node.parent, path_up_tree)
        else:
            z, y, x = current_node, path_up_tree[-1], path_up_tree[-2]
            # CASE 1
            if z.left_child is y and y.left_child is x:
                self.right_rotate(node=z)
                self.__update_heights(current_node=self.root)
            # CASE 2
            elif z.left_child is y and y.right_child is x:
                self.left_rotate(node=y)
                self.right_rotate(node=z)
                self.__update_heights(current_node=self.root)
            # CASE 3
            elif z.right_child is y and y.right_child is x:
                self.left_rotate(node=z)
                self.__update_heights(current_node=self.root)
            # CASE 4
            else:
                self.right_rotate(node=y)
                self.left_rotate(node=z)
                self.__update_heights(current_node=self.root)

    ###################
    # MAIN OPERATIONS #
    ###################

    def delete(self, key, current_node=None, start=True):
        # 1. Delete the node & recurse on parent
        if start is True:
            current_node = self.find(key=key, current_node=self.root)
            if current_node.right_child.key is not None:
                self.transplant(current_node, current_node.right_child)
                return self.delete(key=key, current_node=current_node.parent, start=False)
            else:
                self.transplant(current_node, current_node.left_child)
                return self.delete(key=key, current_node=current_node.parent, start=False)

        # This means we have popped off the root
        if current_node is None and start is False: return

        # This means this is a leaf node and we need to recurse up
        if current_node.height == 0:
            return self.delete(key, current_node.parent, start=False)
        balance_factor = self.__check_balance_factor(current_node)
        if balance_factor < 2:
            return self.delete(key=key, current_node=current_node.parent, start=False)
        else:
            z, y, x = current_node, current_node.max_height_child, current_node.max_height_child.max_height_child
            # CASE 1
            if z.left_child is y and y.left_child is x:
                self.right_rotate(node=z)
                self.__update_heights(current_node=self.root)
                return self.delete(key, current_node=z.parent, start=False)
            # CASE 2
            elif z.left_child is y and y.right_child is x:
                self.left_rotate(node=y)
                self.right_rotate(node=z)
                self.__update_heights(current_node=self.root)
                return self.delete(key, current_node=z.parent, start=False)
            # CASE 3
            elif z.right_child is y and y.right_child is x:
                self.left_rotate(node=z)
                self.__update_heights(current_node=self.root)
                return self.delete(key, current_node=z.parent, start=False)
            # CASE 4
            else:
                self.right_rotate(node=y)
                self.left_rotate(node=z)
                self.__update_heights(current_node=self.root)
                return self.delete(key, current_node=z.parent, start=False)



if __name__ == '__main__':
    # [41, 38, 31, 12, 19, 8]
    avl_tree = AVLTree(init_items=[31, 38, 41, 19, 8, 52])

    # items_to_delete = [8, 12, 19, 31, 38, 41]
    items_to_delete = [19]
    for item in items_to_delete:
        avl_tree.delete(item)

    print("Done")

