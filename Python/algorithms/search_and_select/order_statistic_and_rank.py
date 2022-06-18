from data_structures.trees.order_statistic_tree import OrderStatisticTree


def find_ith_stat(current_node, i):
    if current_node is None or current_node.key is None:
        return None
    r = current_node.left_child.size + 1
    if i == r:
        return current_node
    elif i < r:
        return find_ith_stat(current_node=current_node.left_child, i=i)
    else:
        return find_ith_stat(current_node=current_node.right_child, i=i - r)


def find_ith_rank(os_tree, current_node, rank):
    if current_node is os_tree.root:
        return rank
    else:
        if current_node is current_node.parent.right_child:
            rank += current_node.parent.left_child.size + 1
        return find_ith_rank(os_tree=os_tree, current_node=current_node.parent, rank=rank)


if __name__ == '__main__':
    os_tree = OrderStatisticTree(init_items=[41, 38, 31, 12, 19, 8])

    ith_stat_node = find_ith_stat(current_node=os_tree.root, i=6)
    print(f"The 6th smallest node in tree has key: {ith_stat_node.key}")

    ith_rank = find_ith_rank(os_tree, current_node=ith_stat_node, rank=ith_stat_node.left_child.size + 1)
    print(f"Node has rank: {ith_rank}")
