#This is written by Yuchen Yan for comp9021 lab4

'''
encode and decode
'''

def right(a,b):
    a += 1
    b = b
    return [a,b]

def up(a,b):
    a = a
    b += 1
    return [a,b]

def left(a,b):
    a -= 1
    b = b
    return [a,b]

def down(a,b):
    a = a
    b -= 1
    return[a,b]



def encode(a,b):
    incremental1 = 1
    incremental2 = 2 
    i = 0
    L = [0,0]
    flag = False
    while True:
        for _ in range(incremental1):
            L = right(L[0],L[1])
            i += 1
            if L[0] == a and L[1] == b:
                flag = True
                break
        if flag:
            break

        
            
        for _ in range(incremental1):
            L = up(L[0],L[1])
            i += 1
            if L[0] == a and L[1] == b:
                flag = True
                break
        if flag:
            break

        incremental1 += 2

            
        for _ in range(incremental2):
            L = left(L[0],L[1])
            i += 1
            if L[0] == a and L[1] == b:
                flag = True
                break
        if flag:
            break


            
        for _ in range(incremental2):
            L = down(L[0],L[1])
            i += 1
            if L[0] == a and L[1] == b:
                flag = True
                break
        if flag:
            break
        incremental2 += 2

            
    return i

    
        
 
    







def decode(n):
    incremental1 = 1
    incremental2 = 2 
    i = 0
    L = [0,0]
    flag = False
    while True:
        for _ in range(incremental1):
            L = right(L[0],L[1])
            i += 1
            if i >= n:
                flag = True
                break
        if flag:
            break

        
            
        for _ in range(incremental1):
            L = up(L[0],L[1])
            i += 1
            if i >= n:
                flag = True
                break
        if flag:
            break

        incremental1 += 2

            
        for _ in range(incremental2):
            L = left(L[0],L[1])
            i += 1
            if i >= n:
                flag = True
                break
        if flag:
            break


            
        for _ in range(incremental2):
            L = down(L[0],L[1])
            i += 1
            if i >= n:
                flag = True
                break
        if flag:
            break
        incremental2 += 2

            
    return(L[0],L[1])








print(encode(-2,-2))











        


        
