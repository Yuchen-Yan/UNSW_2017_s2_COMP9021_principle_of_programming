# Insert your code here
#Written by Yuchen Yan Vincent for comp9021_assignment1_question1

'''
This program is aim to prompts the user for a natural number N at least
equal to 1, and outputs the numbers at the top, the front and the right
after the die has been moved to cell N
'''


def input_cell():
    while True:
        try:
            input_value = int(input('Enter the desired goal cell number: '))
            if input_value < 1:
                raise ValueError
            return input_value
        except ValueError:
            print('Incorrect value, try again')

            

def move_up(T,F,R):
    opposite = {1:6 ,2:5 ,3:4 ,4:3 ,5:2 , 6:1}
    f = opposite[T]
    t = F
    r = R        
    return(t,f,r)


def move_down(T,F,R):
    opposite = {1:6 ,2:5 ,3:4 ,4:3 ,5:2 , 6:1}
    t = opposite[F]
    f = T
    r = R
    return(t,f,r)


def move_right(T,F,R):
    opposite = {1:6 ,2:5 ,3:4 ,4:3 ,5:2 , 6:1}
    t = opposite[R]
    r = T
    f = F
    return(t,f,r)


def move_left(T,F,R):
    opposite = {1:6 ,2:5 ,3:4 ,4:3 ,5:2 , 6:1}
    r = opposite[T]
    t = R
    f = F
    return(t,f,r)



incremental_1 = 1
incremental_2 = 2
flag = False

if __name__ == '__main__':
    N = input_cell()    
    t = 3
    r = 1
    f = 2
    i = 0
    if N == 1:
        pass
    else:
        while True:
            for mr in range(1, incremental_1+1):  
                (t,f,r) = move_right(t,f,r)
                i += 1 
                if i >= N-1:
                    flag = True
                    break
            if flag:
                break
        

    
            for md in range(1, incremental_1+1):
                (t,f,r) = move_down(t,f,r)
                i += 1
                if i >= N-1:
                    flag = True
                    break
            if flag:
                break
            
            incremental_1 += 2



            for ml in range(1, incremental_2+1):
                (t,f,r) = move_left(t,f,r)
                i += 1 
                if i >= N-1:
                    flag = True
                    break
            if flag:
                break



            for mu in range(1, incremental_2+1):
                (t,f,r) = move_up(t,f,r)
                i += 1
                if i == N-1:
                    flag = True
                    break
            if flag:
                break
        
            incremental_2 += 2
    
    print(f'On cell {N}, {t} is at the top, {f} at the front, and {r} on the right.')


















    

