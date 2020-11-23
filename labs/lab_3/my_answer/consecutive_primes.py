#this is writen by Yuchen Yan

'''
This is aim to finds all sequences of 6 consecutive prime
'''
from math import sqrt

'''
primes = [True] *100001

for n in range(2, round(sqrt(100000))+1):
    if primes[n]:
        for i in range(n*n, 100001, n):
            primes[i] = False
'''
N = 100000

primes = [True] * (N + 1)
for n in range(2, round(sqrt(N)) + 1):
    if primes[n]:
        for i in range(n * n, N + 1, n):
            primes[i] = False

L = []
for j in range(10000, 100000):
    if primes[j] and j < 99990:
        if primes[j]==True and primes[j+2]==True and primes[j+6]==True and\
           primes[j+12]==True and primes[j+20]==True and primes[j+30]==True:
            L.append([j,j+2,j+6,j+12,j+20,j+30])

for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end = ' ')
    print()


