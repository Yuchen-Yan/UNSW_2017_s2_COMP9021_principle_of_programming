# Written by Vincent Yuchen Yan for comp9021 lab1

'''
generates a list of nb_of_elements random integers between
- 50 and 50, prints out the list,
computes the mean, the median and the standard deviation in two ways
'''
from random import randint
import sys
import math
import numpy as np


seedd = input('Input a seed for the random number generator: ')
try:
    seedd = int(seedd)
except ValueError:
    print('Input must be an integer, giving up')
    sys.exit()


nb_of_element = input('How many elements do you want to generate?')
try:
    nb_of_element = int(nb_of_element)
except ValueError:
    print('Input must be an integer, giving up')
    sys.exit()

if nb_of_element <= 0:
    print('input must be an positive number, giving up')
    sys.exit()
L = [randint(-50,50) for _ in range(nb_of_element)]

print('\nThis is the List:', L)




#the mean calculation
sums = 0
for i in range(nb_of_element):
    sums += L[i]
mean = sums/(i+1)
print(f'\nThe mean is:{mean:7.2f}')




#the media calculation
for j in range(0,len(L)):
    minimum = j
    for k in range(j+1,len(L)):
        if L[minimum]>L[k]:
            minimum = k
    L[j],L[minimum] = L[minimum],L[j]
    
if nb_of_element % 2 == 1:
    print(f'The median is: {L[nb_of_element//2]:7.2f}')
else:
    media = (L[nb_of_element//2]+L[nb_of_element//2-1])/2
    print(f'The median is: {media:7.2f}')    




#the standard deviation calculation
variance = 0
for x in range(nb_of_element):
    variance += (L[x]-mean)*(L[x]-mean)
variance /= int(nb_of_element)
s_d = math.sqrt(variance)
print(f'The standard deviation is {s_d:7.2f}')



#check by numpy modulo
print('\nConfirming with functions from the statistics module:')
print(f'\nThe mean is {np.mean(L):7.2f}')
print(f'The median is {np.median(L):7.2f}')
print(f'The standard deviation is {np.std(L):7.2f}')


