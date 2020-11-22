# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers smaller than the length of L,
whose value is input by the user, and outputs two lists:
- a list M consisting of L's middle element, followed by L's first element,
  followed by L's last element, followed by L's second element, followed by
  L's penultimate element...;
- a list N consisting of L[0], possibly followed by L[L[0]], possibly followed by
  L[L[L[0]]]..., for as long as L[L[0]], L[L[L[0]]]... are unused, and then,
  for the least i such that L[i] is unused, followed by L[i], possibly followed by
  L[L[i]], possibly followed by L[L[L[i]]]..., for as long as L[L[i]], L[L[L[i]]]...
  are unused, and then, for the least j such that L[j] is unused, followed by L[j],
  possibly followed by L[L[j]], possibly followed by L[L[L[j]]]..., for as long as
  L[L[j]], L[L[L[j]]]... are unused... until all members of L have been used up.
'''


import sys
from random import seed, randrange


try:
    arg_for_seed, length = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length = int(arg_for_seed), int(length)
    if arg_for_seed < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randrange(length) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)
M = []
N = []











# Replace this comment with your code
#Generate list M
if L!=[]:
    x = length//2
    M.append(L[x])
    x = 0
    y = len(L)-1
    for i in range(0,len(L)-1):
        M.append(L[x])    
        x += (-1)**i*y
        y -= 1
else:
    M = []

#Generate list N
N_2 = []
if L!=[]:
    N.append(L[0])
    while len(N) != len(L):
        if N[-1] !=0 and N[-1] not in [item_1 for index_1, item_1 in enumerate(N) if index_1 !=len(N)-1]+N_2:
            N.append(L[N[-1]])
        else:       
            for index_2, item_2 in enumerate(L):
                if index_2 != 0 and index_2 not in N+N_2:
                    N_2.append(index_2)
                    N.append(item_2)
                    break


else:
    N=[]





	
	
	
	
	


    
print('\nHere is M:')
print('  ', M)
print('\nHere is N:')
print('  ', N)
print('\nHere is L again:')
print('  ', L)

