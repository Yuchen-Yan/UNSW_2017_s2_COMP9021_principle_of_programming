# Weitten by Yuchen Yan Vincent for comp9021 lab2

'''


'''
import sys
from random import randint
try:
    times = int(input('Enter the desired number of times a randomly chosen die will be cast: '))
except ValueError:
    sys.exit()




face = [4,6,8,12,20]

for i in range(1,times+1):
    p = [0.2,0.2,0.2,0.2,0.2]
    if i == 1:
        die = face[randint(0,4)]
        print(f'\nThis is a secret, but the chosen die is the one with {die} faces\n')
    if i <= 5:
        print(f'Casting the chosen die... Outcome: {randint(1,die)}')
        print('The updated dice probabilities are:')
        print('         4: {p[0]:.2f}%')
        print('         6: {p[1]:.2f}%')
        print('         8: {p[2]:.2f}%')
        print('        12: {p[3]:.2f}%')
        print('        20: {p[4]:.2f}%\n\n\n')


        
print('The final probabilities are:')
print('         4: {p[0]:.2f}%')
print('         6: {p[1]:.2f}%')
print('         8: {p[2]:.2f}%')
print('        12: {p[3]:.2f}%')
print('        20: {p[4]:.2f}%')
