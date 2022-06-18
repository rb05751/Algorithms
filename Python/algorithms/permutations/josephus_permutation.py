from data_structures.circular_doubly_linked_list import CircularDoublyLinkedList


class JosephusList(CircularDoublyLinkedList):

    def __len__(self):
        i = 0
        current = self.nil.next
        while current.data != None:
            i += 1
            current = current.next
        return i

    def delete(self, x):
        if x.data is not None:
            if x.next.data is None:
                x.prev.next = x.next
                x.prev, x.next = None, None
            else:
                x.prev.next = x.next
                x.next.prev = x.prev
                x.next, x.prev = None, None
        else:
            return f"Item does not exist"
        return x


def josephus_permutation(n, m, list_of_items, permuted_list, current_node):

    if list_of_items is None:
        list_of_items = JosephusList(init_items=list(range(1, n + 1)))
        current_node = list_of_items.nil.next

    if len(list_of_items) == 0:
        return permuted_list

    else:
        i = 1
        while i < m:
            current_node = current_node.next
            if current_node.data is None: continue
            i += 1

        # Lets not allow it to start on the Sentinel, it messes with the counting
        new_starting_node = current_node.next if current_node.next.data is not None else current_node.next.next
        list_of_items.delete(x=current_node)
        permuted_list.append(current_node.data)
        return josephus_permutation(n, m, list_of_items, permuted_list, new_starting_node)


if __name__ == '__main__':
    permuted_items = josephus_permutation(n=7, m=3, list_of_items=None, permuted_list=[], current_node=None)

    print(permuted_items)
