#this is writtrn by Yuchen YAN for lab 4

'''
Give the height N
print the triangle of height N
'''
while True:
    try:
        N = int(input('Enter strictly positive number: '))
        if N <= 0:
            raise ValueError
        break
    except ValueError:
        print('Wrong input, please input again...')



var = 65

for i in range(1,N+1):
    for _ in range(N-i):
        print(' ', end = '')

    L = []
    for _ in range(i):
        if var == 91:
            var = 65
        print(chr(var), end = '')
        L.append(chr(var))
        var += 1
        
    L.pop(-1)       
    for _ in range(i-1):
        print(L.pop(-1), end = '')
        
    for _ in range(N-i):
        print(' ', end = '')
    print('')
        
    
