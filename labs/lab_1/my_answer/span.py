# wrirtten by Yuchen Yan for COMP9021 lab1

'''
Prompts the user for a seed for the random number generator,
and for a strictly positive number, nb_of_elements.
Generates a list of nb_of_elements random integers between 0 and 99,
prints out the list, computes the maximum element of the list without using the
builtin max(), prints it out, and confirms that the value is correct with the builtin.
'''

from random import seed, randint

seedd = input('Input a seed for the random number generator: ')
try:
    seedd = int(seedd)
except ValueError:
    print('Intput is not a integer, giving up')
    sys.exit()




nb_for_member = input('How many elements do you want to generate? ')
try:
    nb_for_member=int(nb_for_member)
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()


if nb_for_member <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()





seed(seedd)
L = [randint(0,99) for _ in range(nb_for_member)]
print('\nThe list is:', L)

max_element = 0
for e in L:
    if e > max_element:
        max_element = e
min_element = 100
for e in L:
    if e < min_element:
        min_element = e

difference = max_element-min_element
print('\nThe maximum difference between largest and smallest values in this list is: ', difference)


 
print('Confirming with builtin operations: ', max(L)-min(L))

