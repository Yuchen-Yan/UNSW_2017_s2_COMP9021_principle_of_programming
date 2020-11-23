from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def remove_duplicates(self):
        '''
        >>> LL = ExtendedLinkedList()
        >>> LL.remove_duplicates()
        >>> LL.print()
        >>> LL = ExtendedLinkedList([1])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1
        >>> LL = ExtendedLinkedList([1, 1])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1
        >>> LL = ExtendedLinkedList([1, 1, 1])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1
        >>> LL = ExtendedLinkedList([1, 1, 1, 2, 2, 2])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1, 2
        >>> LL = ExtendedLinkedList([1, 2, 1, 2, 1, 2])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1, 2
        >>> LL = ExtendedLinkedList([1, 2, 3])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1, 2, 3
        >>> LL = ExtendedLinkedList([1, 1, 1, 2, 1, 2, 1, 2, 3, 3, 2, 1])
        >>> LL.remove_duplicates()
        >>> LL.print()
        1, 2, 3
        '''
        if not self.head:
            return
        current = self.head
        while current:
            node = current
            while node.next_node:
                if current.value == node.next_node.value:
                    node.next_node = node.next_node.next_node
                else:
                    node = node.next_node
            current = current.next_node

        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
