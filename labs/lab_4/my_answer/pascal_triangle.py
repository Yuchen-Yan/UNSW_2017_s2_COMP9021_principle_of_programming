#this is wirrten by Yuchen Yan for lab4 question 2

'''
Print the pascal triangle
'''
from math import factorial

try:
    N = int(input('Enter a nonnegative integer: '))
    if N <= 0:
        raise ValueError
except ValueError:
    print('Wrong input, exiting....')


if (N+1) % 2 == 0:
    n = N
    m = (N+1)/2 
else:
    n = N
    m = (N+2)/2 - 1

big = int(factorial(n)/(factorial(m)*factorial(n-m)))

place = 2 * len(str(big))
width = place*N + 1
L = []

for i in range(1,N+2):
    blank = ((width - 1)-(i-1)*place)/2
    for _ in range(int(blank)):
        print(' ', end = '')

    
    T = []
    for e in range(i):
        if e == 0:
            print(1, end = '')
            T.append(1)
        elif e==i-1:
            for _ in range(place-1):
                print(' ', end = '')
            print(1, end = '')
            T.append(1)
            
        else:
            current = L[e]+L[e-1]
            T.append(current)
            blank_i = place - len(str(current))
            for _ in range(int(blank_i)):
                print(' ', end = '')
            print(current, end = '')
    L = T

    for _ in range(int(blank-1)):
        print(' ', end = '')
    print(' ')

    #print(L)
        
        
