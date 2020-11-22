
from priority_queue_adt import *


L = [66, 91, 10, 107, 122, 35, 55, 77, 130, 98, 149, 124, 129, 72, 103]

pq = PriorityQueue()
for e in L:
    pq.insert(e)

    
pq1 = PriorityQueue()
for e in pq._data[1:len(pq)+1]:
    pq1.insert(e)

if pq1._data == pq._data:
    print('work')
