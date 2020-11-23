#This is written by Yuchen Yan for comp9021 lab4


'''
Contains five functions which are print_square(square), is_magic_square(square),
bachet_magic_square(n), siamese_magic_square(n), and, finally, lux_magic_square(n).
'''

from random import randint

def print_square(square):
    new = []
    for i in range(len(square)):
        for j in range(len(square)):
            new.append(square[i][j])
    place = len(str(max(new)))+1


            
    for i in range(len(square)):
        for j in range(len(square)):
            
            if j == len(square[i])-1:
                for e in range(place-len(str(square[i][j]))):
                    print(' ', end = '')                
                print(square[i][j], end = '\n')
            else:
                for e in range(place-len(str(square[i][j]))):
                    print(' ', end = '')
                print(square[i][j], end = '')



def is_magic_square(square):
#check rows
    row = False
    r = []
    sum_r = 0
    for i in range(len(square)):
        for j in range(len(square[i])):
            sum_r += square[i][j]
        r.append(sum_r)
        sum_r = 0
    if r.count(r[0]) == len(r):
        row = True   
#check columns
    column = False
    c = []
    sum_c = 0
    for i in range(len(square)):
        for j in range(len(square)):
            sum_c += square[j][i]
        c.append(sum_c)
        sum_c = 0
    if c.count(c[0]) == len(c):
        column = True
#check diagonals
    diagonal = False
    d = []
    sum_d = 0
    for i in range(len(square)):
        sum_d += square[i][i]
    d.append(sum_d)

    sum_d = 0
    e = len(square) - 1
    for j in range(len(square)):
        sum_d += square[e][j]
        e -= 1
    d.append(sum_d)
    if d[0] == d[1]:
        diagonal = True
        

    if row == True and column == True and diagonal == True:
        return True
    else:
        return False









def bachet_magic_square(n):    
    square = [[0 for _ in range(2*n-1)] for _ in range(2*n-1)]
    digit = 1
    for i in range(n):
        for j in range(n):
            square[i+j][n-1-i+j] = digit
            digit += 1
    
    for i in range(n//2):
        for j in range(2*n-1):
            if square[i][j] != 0:
                square[i+n][j] = square[i][j]
                square[i][j] = 0

    square_1 = [[0 for i in range(len(square))] for j in range(len(square))]
    for i in range(2*n-1):
        for j in range(2*n-1):
            square_1[j][(2*n-2) - i] = square[i][j]


    return square_1








def siamese_magic_square(n):
    square = [[0 for _ in range(n)] for _ in range(n)]
    i = 0
    j = n//2
    for e in range(1, n**2+1):
        if e == 1:
            square[i][j] = e
            continue
            
        if i == 0 and j != n-1:
            if square[n-1][j+1] == 0:
                i = n-1
                j += 1
                square[i][j] = e
            elif square[n-1][j+1] != 0:
                i += 1
                square[i][j] = e
        elif i ==0 and j ==n-1:
            if square[n-1][0] == 0:
                i = n-1
                j = 0
                square[i][j] = e
            elif square[n-1][0] != 0:
                i = 1
                square[i][j] = e
        elif i == n-1 and j != n-1:
            if square[i-1][j+1] == 0:
                i -= 1
                j += 1
                square[i][j] = e
            elif square[i-1][j+1] != 0:
                i = 0
                square[i][j] = e
        elif i == n-1 and j == n-1:
            if square[i-1][0] == 0:
                i -= 1
                j = 0
                square[i][j] = e
            elif square[i-1][0] != 0:
                i = 0
                square[i][j] = e
                
        elif j == n-1:
            if square[i-1][0] == 0:
                i -= 1
                j = 0
                square[i][j] = e
            elif square[i-1][0] != 0:
                i += 1
                square[i][j] = e

        else:               
            if square[i-1][j+1]==0:
                i -= 1
                j += 1
                square[i][j] = e
            elif square[i-1][j+1] != 0:
                i += 1
                square[i][j] = e
    return square
        









def lux_magic_square(n):
    k = (n-2)/4
    k = int(k)
    square = [[0 for _ in range(2*k+1)] for _ in range(2*k+1)]
    for i in range(2*k+1):
        for j in range(2*k+1):
            if i in range(k+1):
                square[i][j] = 'L'
            elif i == k+1:
                square[i][j] = 'U'
            else:
                square[i][j] = 'X'
    square[k][k],square[k+1][k] = square[k+1][k],square[k][k]

    i = 0
    j = (2*k+1)//2
    #print(i,j)
    n = 2*k+1
    e = 0
    for x in range(0, (2*k+1)**2):
        if x == 0:
            square[i][j] = [e+4,e+1,e+2,e+3]
            e = max(square[i][j])
            continue
            
        if i == 0 and j != n-1:
            #print(x)
            if square[n-1][j+1] == 'L' or square[n-1][j+1] == 'U' or square[n-1][j+1] == 'X':
                i = n-1
                j += 1
                
                if square[i][j] == 'L':
                    square[i][j] = [e+4,e+1,e+2,e+3]
                elif square[i][j] == 'U':
                    square[i][j] = [e+1,e+4,e+2,e+3]
                elif square[i][j] == 'X':
                    square[i][j] = [e+1,e+4,e+3,e+2]
 
                e = max(square[i][j])
            else:
                print(x)
                i += 1
                if square[i][j] == 'L':
                    square[i][j] = [e+4,e+1,e+2,e+3]
                elif square[i][j] == 'U':
                    square[i][j] = [e+1,e+4,e+2,e+3]
                elif square[i][j] == 'X':
                    square[i][j] = [e+1,e+4,e+3,e+2]
                e = max(square[i][j])

                
        elif i ==0 and j ==n-1:
            if square[n-1][0] == 'L' or square[n-1][0] == 'U' or square[n-1][0] == 'X':
                i = n-1
                j = 0
                if square[i][j] == 'L':
                    square[i][j] = [e+4,e+1,e+2,e+3]
                elif square[i][j] == 'U':
                    square[i][j] = [e+1,e+4,e+2,e+3]
                elif square[i][j] == 'X':
                    square[i][j] = [e+1,e+4,e+3,e+2]
                e = max(square[i][j])
            else:
                i = 1
                if square[i][j] == 'L':
                    square[i][j] = [e+4,e+1,e+2,e+3]
                elif square[i][j] == 'U':
                    square[i][j] = [e+1,e+4,e+2,e+3]
                elif square[i][j] == 'X':
                    square[i][j] = [e+1,e+4,e+3,e+2]
                e = max(square[i][j])

                
        elif i == n-1 and j != n-1:
            if square[i-1][j+1] == 'L' or square[i-1][j+1] == 'U' or square[i-1][j+1] == 'X':
                i -= 1
                j += 1
                if square[i][j] == 'L':
                    square[i][j] = [e+4,e+1,e+2,e+3]
                elif square[i][j] == 'U':
                    square[i][j] = [e+1,e+4,e+2,e+3]
                elif square[i][j] == 'X':
                    square[i][j] = [e+1,e+4,e+3,e+2]
                e = max(square[i][j])
            else:
                i = 0
                if square[i][j] == 'L':
                    square[i][j] = [e+4,e+1,e+2,e+3]
                elif square[i][j] == 'U':
                    square[i][j] = [e+1,e+4,e+2,e+3]
                elif square[i][j] == 'X':
                    square[i][j] = [e+1,e+4,e+3,e+2]
                e = max(square[i][j])

                
        elif i == n-1 and j == n-1:
            if square[i-1][0] == 'L' or square[i-1][0] == 'U' or square[i-1][0] == 'X':
                i -= 1
                j = 0
                if square[i][j] == 'L':
                    square[i][j] = [e+4,e+1,e+2,e+3]
                elif square[i][j] == 'U':
                    square[i][j] = [e+1,e+4,e+2,e+3]
                elif square[i][j] == 'X':
                    square[i][j] = [e+1,e+4,e+3,e+2]
                e = max(square[i][j])
            else:
                i = 0
                if square[i][j] == 'L':
                    square[i][j] = [e+4,e+1,e+2,e+3]
                elif square[i][j] == 'U':
                    square[i][j] = [e+1,e+4,e+2,e+3]
                elif square[i][j] == 'X':
                    square[i][j] = [e+1,e+4,e+3,e+2]
                e = max(square[i][j])
                
        elif j == n-1:
            if square[i-1][0] == 'L' or square[i-1][0] == 'U' or square[i-1][0] == 'X':
                i -= 1
                j = 0
                if square[i][j] == 'L':
                    square[i][j] = [e+4,e+1,e+2,e+3]
                elif square[i][j] == 'U':
                    square[i][j] = [e+1,e+4,e+2,e+3]
                elif square[i][j] == 'X':
                    square[i][j] = [e+1,e+4,e+3,e+2]
                e = max(square[i][j])
            else:
                i += 1
                if square[i][j] == 'L':
                    square[i][j] = [e+4,e+1,e+2,e+3]
                elif square[i][j] == 'U':
                    square[i][j] = [e+1,e+4,e+2,e+3]
                elif square[i][j] == 'X':
                    square[i][j] = [e+1,e+4,e+3,e+2]
                e = max(square[i][j])


        else:
            if square[i-1][j+1]=='L' or square[i-1][j+1]=='U' or square[i-1][j+1]=='X':
                i -= 1
                j += 1
                if square[i][j] == 'L':
                    square[i][j] = [e+4,e+1,e+2,e+3]
                elif square[i][j] == 'U':
                    square[i][j] = [e+1,e+4,e+2,e+3]
                elif square[i][j] == 'X':
                    square[i][j] = [e+1,e+4,e+3,e+2]
                e = max(square[i][j])
            else:
                i += 1
                if square[i][j] == 'L':
                    square[i][j] = [e+4,e+1,e+2,e+3]
                elif square[i][j] == 'U':
                    square[i][j] = [e+1,e+4,e+2,e+3]
                elif square[i][j] == 'X':
                    square[i][j] = [e+1,e+4,e+3,e+2]
                e = max(square[i][j])
    

    
    odd = []
    Odd = []
    for i in range(2*k+1):
        for j in range(2*k+1):
            for x in range(2):
                odd.append(square[i][j][x])
        Odd.append(odd)
        odd = []
    even = []
    Even = []
    for i in range(2*k+1):
        for j in range(2*k+1):
            for x in range(2,4):
                even.append(square[i][j][x])
        Even.append(even)
        even = []
        
        Square = []
    for i in range(len(Even)):
        Square.append(Odd[i])
        Square.append(Even[i])
        
    return Square

    





















#square = [[2,7,6],[9,5,1],[4,3,8]]    
#square = [[1,23,1,1,1,1],[2,2,12,2,2,2],[3,3,3,3,3,3],[4,4,4,4,4,4],[5,5,5,5,5,5],[6,6,6,6,6,6]]

#print_square(square)
#print(is_magic_square(square))
#print_square(bachet_magic_square(7))
#print_square(siamese_magic_square(9))
#for i in range(len(lux_magic_square(10))):
#    print(lux_magic_square(10)[i])

#print_square(lux_magic_square(6))
