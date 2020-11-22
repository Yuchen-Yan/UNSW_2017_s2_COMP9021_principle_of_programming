# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains then 1/2, then the fact that 1/2 belongs to "fractions";
- otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
  if that member is unique;
- otherwise, the two members "closest_1" and "closest_2" of "fractions" that are closest to 1/2,
  in their natural order.
'''


import sys
from random import seed, randint
from math import gcd


try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions = []
spot_on, closest_1, closest_2 = [None] * 3

# Replace this comment with your code
#find all the fractions
L_1 = []
min_upper = 1
min_lower = 1


if len(L) == 1:
    closest_1 = 1

for index_1, item_1 in enumerate(L):
    for index_2, item_2 in enumerate(L):
        if index_2 != index_1:
            if item_2 != 0 and item_1/item_2 <= 1:
                g = gcd(item_1,item_2)
                a , b = item_1/g , item_2/g
                a , b = int(a), int(b)
                if a/b == 0 and '0' not in fractions:
                    fractions.append('0')
                    L_1.append(0)
                elif a/b == 1 and '1' not in fractions:
                    fractions.append('1')
                    L_1.append(1)
                elif f'{a}/{b}' not in fractions and a/b != 1 and a/b != 0:
                    fractions.append(f'{a}/{b}')
                    L_1.append(a/b)


#find the minimum fractions close to 1/2

for index_3, item_3 in enumerate(L_1):
    if item_3 == 0.5:
        spot_on = True
        break
    elif item_3 > 0.5:
        if item_3 - 0.5 < min_upper:
            min_num1 = item_3 
            min_upper = item_3 -0.5
            min_index1 = index_3
    elif item_3 < 0.5:
        if 0.5 - item_3 < min_lower:    
            min_num2 = item_3
            min_lower = 0.5 - item_3
            min_index2 = index_3


if int(len(L_1)) != 0 and (min_lower != 1 or min_upper != 1) :
    if min_lower == min_upper:
        closest_1 = fractions[min_index2]
        closest_2 = fractions[min_index1]
    elif min_lower < min_upper:
        closest_1 = fractions[min_index2]
    else:
        closest_1 = fractions[min_index1]




#Ranking the fractions from smallest to largest
for index_4 in range(0, len(L_1)):
    for index_5 in range(index_4+1, len(L_1)):
            if L_1[index_4] > L_1[index_5]:
                L_1[index_4], L_1[index_5] =  L_1[index_5], L_1[index_4]
                fractions[index_4],fractions[index_5] = fractions[index_5],fractions[index_4]
                


if '1' not in fractions:
    fractions.append('1')


#end of my code
















print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:')
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')

