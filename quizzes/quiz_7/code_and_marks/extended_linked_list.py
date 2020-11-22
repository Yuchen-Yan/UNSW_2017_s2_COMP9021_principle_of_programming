# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        flag = True
        flag2 = True
        if not self.head:
            return
        n = self.head
        n1 = self.head
       
        all_even = True
        all_odd  = True
        while n1:
            if n1.value%2:
                all_even = False 
            elif not n1.value%2:
                all_odd = False
            n1 = n1.next_node
        if all_even:
            return
        elif all_odd:
            return
                
        while n:
            if n.value%2 and flag:
                node = n
                self.head = node
                flag = False
            elif not n.value%2 and flag2:
                node2 = n
                head2 = node2
                flag2 = False
            elif n.value%2:
                node.next_node = n
                node = node.next_node
            elif not n.value%2:
                node2.next_node = n
                node2 = node2.next_node
            n = n.next_node



        node2.next_node = None
        node.next_node = head2
            

        
            
        



    
    
    



        
            
        



    
    
    


