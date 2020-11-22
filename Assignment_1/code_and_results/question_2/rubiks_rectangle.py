# This is written by Yuchen Yan for comp9021 assignment1 question 2

'''
Outputs the number of steps needed to reach the final configuration
(this is always possible), using a message whose grammatical form
depends on whether the number of steps is 0 or 1, or at least 2.
'''

from collections import deque


def input_final():
    L=[]
    try:
        input_value = input('Input final configuration: ')
        list(input_value)
        for e in input_value:
            if e != ' ':
                if e in ['1','2','3','4','5','6','7','8']:
                    L.append(e)
                else:
                    raise ValueError
        
        for index, item in enumerate(L):
            for index_1, item_1 in enumerate(L):
                if index != index_1:
                    if item == item_1:
                        raise ValueError
                
        if len(L)!= 8:
            raise ValueError
                
    except ValueError:
        print('Incorrect configuration, giving up...')
        exit()
    return L






def row_exchange(k1,k2,k3,k4,k5,k6,k7,k8):
    return (k8,k7,k6,k5,k4,k3,k2,k1)
    
def right_circular(k1,k2,k3,k4,k5,k6,k7,k8):
    return (k4,k1,k2,k3,k6,k7,k8,k5)

def middle_clockwise(k1,k2,k3,k4,k5,k6,k7,k8):
    return (k1,k7,k2,k4,k5,k3,k6,k8)









def BFS(k1,k2,k3,k4,k5,k6,k7,k8):
    final = (k1,k2,k3,k4,k5,k6,k7,k8)
    init = ('1','2','3','4','5','6','7','8')
    if final == init:
        return 0

    #time = 0
    #i = 0
    the_deque = deque()
    the_deque.append((init,0))
    repeat = []
    while the_deque:

        (pop, time)= the_deque.popleft()
        if pop in repeat:
            continue
        else:
            repeat.append(pop)
            time +=1
            middle = middle_clockwise(pop[0],pop[1],pop[2],pop[3],pop[4],pop[5],pop[6],pop[7])
            right = right_circular(pop[0],pop[1],pop[2],pop[3],pop[4],pop[5],pop[6],pop[7])
            row = row_exchange(pop[0],pop[1],pop[2],pop[3],pop[4],pop[5],pop[6],pop[7])
            the_deque.append((middle,time))
            the_deque.append((right,time))
            the_deque.append((row,time))
            if middle == final:
                return time
            elif right == final:
                return time
            elif row == final:
                return time
    














if __name__ == '__main__':
    L = []
    L = input_final()
    steps = BFS(L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7])




    if steps == 0 or steps == 1:
        print(f'{steps} step is needed to reach the final configuration.')        
    else:
        print(f'{steps} steps are needed to reach the final configuration.')













