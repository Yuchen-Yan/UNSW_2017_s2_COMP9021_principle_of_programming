# Written by Vincent Yuchen YAN for comp9021 lab2

'''
There are three methods to compute the number of
trailing 0s in the factorial of a number N at least equal to 5
'''

import math


# The three methods of calculate the factorial
def factorial_1(n):
    if n == 1:
        return 1
    return n*factorial_1(n-1)

def factorial_2(n):
    f_2 = 1
    for i in range(1,n+1):
        f_2 = f_2 * i
    return f_2

def factorial_3(n):
    f_3 = math.factorial(n)
    return f_3




# The three methods of calculate the trailing of 0s of factorial

def d_by_10(f):
    number_of_0 = 0
    while True:
        if f%10 == 0:
            number_of_0 += 1
            f = f//10
        else:
            break
    return number_of_0


def string_m(f):
    s_f = str(f)
    number_of_0b = 0
    for i in range(1,len(s_f)+1):
        if s_f[-i] == '0':
            number_of_0b += 1
        else:
            break
    return number_of_0b


def smart_way(n):
    i = 1
    number_of_0c = 0
    while True:
        if n / (5**i) > 0:
            number_of_0c += n//(5**i)
            i += 1
        else:
            break
    return number_of_0c





# the main function

if __name__ =="__main__":
    try:
        N = int(input('Input a nonnegative integer: '))
        if N < 5:
            raise ValueError
    except ValueError:
        print('Incorrect input, giving up.')

    factorial = factorial_3(N)
    answer_1 = d_by_10(factorial)
    answer_2 = string_m(factorial)
    answer_3 = smart_way(N)

    print(f'Computing the number of trailing 0s in {N}! by dividing by 10 for long enough: {answer_1}')
    print(f'Computing the number of trailing 0s in {N}! by converting it into a string: {answer_2}')
    print(f'Computing the number of trailing 0s in {N}! the smart way: {answer_3}')

















