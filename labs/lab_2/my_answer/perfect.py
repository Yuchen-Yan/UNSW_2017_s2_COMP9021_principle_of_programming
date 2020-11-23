# Written by Vincent Yuchen YAN for comp9021 lab2

'''
This program is aim to input a number n and find the
perfect number from 1 to n.
Implement a naive solution, of quadratic complexity,
so that can deal with small
values of N only.
'''





if __name__ =='__main__':
    
    try :
        N = int(input('Input an integer: '))
        if N  <=  0:
            raise ValueError
    except ValueError:
        print('Incorrect number, and exit')
        exit()
    
    for i in range(2, N+1):
        sum_of_d = 0
        for k in range(1, i):
            if i % k == 0:
                sum_of_d += k 
        if i == sum_of_d:
            print(f'{i} is a perfect number.')


