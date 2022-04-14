"""

- Binary Tree where each left edge traversal equals 0 and right edge traversal == 1.

- Each node stores a bit string

- A preorder tree walk sorts the nodes in lexographical order

"""

from binary_search_tree import Node


class RadixTree:
    def __init__(self, bit_strings):
        self.bit_strings = bit_strings
        self.root = Node(key=None)
        self.__build(strings=bit_strings)

    def __print_tree(self, node):
        print(f"Node: {node.key}")
        if node.left_child is not None:
            print(f"Node: {node.key} Left child: {node.left_child.key}")
            self.__print_tree(node.left_child)
        if node.right_child is not None:
            print(f"Node: {node.key} Right child: {node.right_child.key}")
            self.__print_tree(node.right_child)


    def __build(self, strings=None):
        for bit_string in strings:
            self.insert(bit_string=bit_string, current_node=self.root, idx=0)

    def find(self, key=None, current_node=None, idx=0):
        if idx == 0: current_node = self.root
        if current_node is None: return None

        if current_node.key == key:
            return key
        else:
            if key[idx] == '0':
                return self.find(key=key, current_node=current_node.left_child, idx=idx+1)
            else:
                return self.find(key=key, current_node=current_node.right_child, idx=idx+1)

    def insert(self, bit_string, current_node, idx, string_rep=''):
        if string_rep == bit_string:
            current_node.key = bit_string
            return

        if bit_string[idx] == '0':
            if current_node.left_child is None:
                new_node = Node(key=None, parent=current_node)
                current_node.left_child = new_node
                self.insert(bit_string=bit_string, current_node=new_node, idx=idx+1, string_rep=string_rep+'0')
            else:
                self.insert(bit_string=bit_string, current_node=current_node.left_child, idx=idx+1, string_rep=string_rep+'0')
        else:
            if current_node.right_child is None:
                new_node = Node(key=None, parent=current_node)
                current_node.right_child = new_node
                self.insert(bit_string=bit_string, current_node=new_node, idx=idx+1, string_rep=string_rep+'1')
            else:
                self.insert(bit_string=bit_string, current_node=current_node.right_child, idx=idx+1, string_rep=string_rep+'1')

    def delete(self, bit_string):
        node = self.find(key=bit_string)
        if node is None:
            return "Item not in Tree"
        else:
            node.key = None
            return "Item Has Been Deleted!"

    def __repr__(self):
        self.__print_tree(node=self.root)
        return ""


if __name__ == '__main__':
    radix_tree = RadixTree(bit_strings=['1011', '10', '011', '100', '0'])
    print(radix_tree)
