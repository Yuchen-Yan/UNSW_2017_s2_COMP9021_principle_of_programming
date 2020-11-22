# Randomly generates N distinct integers with N provided by the user,
# inserts all these elements into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last element inserted is as large as
#   possible, and then the penultimate element inserted is as large as possible, etc.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, sample
from priority_queue_adt import *


def delete_next(pq3, number):
    find = pq3._data[:len(pq3)+1]
    i = find.index(number)
    pq3._data[i], pq3._data[pq3._length] = pq3._data[pq3._length], pq3._data[i]
    pq3._length -= 1
    pq3._bubble_down(i)
    if pq3.min_capacity // 2 <= pq3._length <= len(pq3._data) // 4:
        pq3._resize(len(pq3._data) // 2)
    return number
# Possibly define some functions

    
def preferred_sequence():        
    L1 = []
    for i in range(len(pq)):
        pq1 = PriorityQueue()
        for e in pq._data[1:len(pq)+1]:
            pq1.insert(e)
        
        delete = pq1.delete()
        pq1.insert(delete)
        if pq1._data[:len(pq)+1] == pq._data[:len(pq)+1]:
            L1.append(delete)
            pq.delete()
        else:
            for j in range(0,len(pq)):
                L2 = sorted(pq._data[1:len(pq)+1],reverse = True)
                pq2 = PriorityQueue()
                for e in pq._data[1:len(pq)+1]:
                    pq2.insert(e)
                delete2 = delete_next(pq2,L2[j])
                pq2.insert(delete2)
                if pq2._data[:len(pq)+1] == pq._data[:len(pq)+1]:
                    L1.append(delete2)
                    delete_next(pq,delete2)
                    break
    L1.reverse()
    return L1
    # Replace pass above with your code (altogether, aim for around 24 lines of code)


try:
    for_seed, length = [int(x) for x in input('Enter 2 nonnegative integers, the second one '
                                                                             'no greater than 100: '
                                             ).split()
                       ]
    if for_seed < 0 or length > 100:
        raise ValueError
except ValueError:
    print('Incorrect input (not all integers), giving up.')
    sys.exit()    
seed(for_seed)
L = sample(list(range(length * 10)), length)
pq = PriorityQueue()
for e in L:
    pq.insert(e)
print('The heap that has been generated is: ')
print(pq._data[ : len(pq) + 1])
print('The preferred ordering of data to generate this heap by successsive insertion is:')
print(preferred_sequence())


