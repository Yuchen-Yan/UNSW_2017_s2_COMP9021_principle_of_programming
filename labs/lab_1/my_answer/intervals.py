# written by Yuchen Yan Vinceny for comp9021 lab 1

'''
Prompts the user for a strictly positive integer, nb_of_elements,
generates a list of nb_of_elements random integers between 0 and 19, prints out the list,
computes the number of elements strictly less 5, 10, 15 and 20, and prints those out
'''

from random import seed, randrange
import sys

arg_for_seed = input('Input a seed for the random number generator:')
try:
    arg_for_seed = int(arg_for_seed)
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()

nb_for_element = input('How many elements do you want to generate?:')
try:
    nb_for_element = int(nb_for_element)
except ValueError:
    print('Input is not an integer, giving up.:')
    sys.exit()

if nb_for_element <=0:
    print('Input should be strictly positive, giving up')
    sys.exit()

    
seed(arg_for_seed)
L = [randrange(20) for _ in range(nb_for_element)]
print('\nThe list is:', L)
print()

answer = [0]*4
for i in range(nb_for_element):
    answer[L[i]//5] +=1

for i in range(4):
    if answer[i] == 0:
        print('There is no element between',end = ' ')
    elif answer[i] == 1:
        print('There is 1 element between',end = ' ')
    else:
        print(f'There are {answer[i]} elements between',end = ' ')
    print(f'{i*5} and {i*5+4}')
