# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for given step_number >= 1
# and step_size >= 2, the number of stairs of step_number many steps,
# with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest step sizes,
# and for a given step size, from stairs with the smallest number of steps to stairs
# with the largest number of stairs.
#
# Written by Yuchen Yan and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def stairs_in_grid():
    d = defaultdict(list)

# all the possible step size and step number
    for size in range(2,int((dim+1)//2+1)):
        L = []
        for nb in range(1,int((dim-size)//(size-1)+1)):
            width = size+nb*(size-1)
            height = size+(nb-1)*(size-1)
            #print(f'dim:{dim} size:{size} nb:{nb} width:{width} height:{height}')
            #print('')
            stairs = 0


#all the possible initial point with condition this point != 0 
            for i in range(0, int((dim-1)-(height-1))+1):
                for j in range(0, int((dim-1)-(width-1))+1):
                    if i<int(dim) and j<int(dim):
                        if grid[i][j] != 0:                       
#check front and back                        
                            if i >= size - 1 and j >= size - 1 and i <= int((dim-1)-(height-1)-(size-1)) and j <= int((dim-1)-(width-1)-(size-1)):
                                #check
                                if (0 in [grid[i-(size-1)][y] for y in range(j-(size-1),j)] or\
                                   0 in [grid[x][j] for x in range(i-(size-1),i)]) and\
                                   (0 in [grid[x1][j+(width-1)] for x1 in range(i+height,i+height+(size-1))] or\
                                   0 in [grid[i+(height-1)+(size-1)][y1] for y1 in range(j+width,j+width+(size-1))]):
                                    #check whether is stair, stair instances all in list s:
                                    #print(i,j)

                                    
                                    s = []
                                    I = i
                                    J = j
                                    I1 = i
                                    J1 = j
                                    for x2 in range(I,I+height,size-1):
                                        for y2 in range(J+1,J+size):
                                            if x2 < int(dim) and y2 < int(dim):
                                                s.append(grid[x2][y2])
                                        J += size-1
                                    for y3 in range(J1+(size-1),J1+(width-1),size-1):
                                        for x3 in range(I1+1,I1+size):
                                            if x3 < int(dim) and y3 < int(dim):
                                                s.append(grid[x3][y3])
                                        I1 += size-1
                                    if 0 not in s:
                                        #print(i,j)
                                        stairs +=1                                
    
    
    
                                    
     
#compileck back
                            elif (i < size-1 or j < size-1) and (i<=int((dim-1)-(height-1)-(size-1)) and j<=int((dim-1)-(width-1)-(size-1))):
                                #check
                                if (0 in [grid[x1][j+(width-1)] for x1 in range(i+height,i+height+(size-1))] or\
                                   0 in [grid[i+(height-1)+(size-1)][y1] for y1 in range(j+width,j+width+(size-1))]):
                                    #check whether is stair, stair instances all in list s:

                                    
                                    s1 = []
                                    I = i
                                    J = j
                                    I1 = i
                                    J1 = j
                                    for x2 in range(I,I+height,size-1):
                                        for y2 in range(J+1,J+size):
                                            if x2 < int(dim) and y2 < int(dim):
                                                s1.append(grid[x2][y2])
                                        J += size-1
                                    for y3 in range(J1+(size-1),J1+(width-1),size-1):
                                        for x3 in range(I1+1,I1+size):
                                            if x3 < int(dim) and y3 < int(dim):
                                                s1.append(grid[x3][y3])
                                        I1 += size-1
                                    if 0 not in s1:
                                        #print(i,j)
                                        stairs +=1 
    
    
    
    
                                    
    
    
    
                            
#classmethodck front
                            elif (i >int((dim-1)-(height-1)-(size-1))) and j >= size-1:
                                #check
                                if (0 in [grid[i-(size-1)][y] for y in range(j-(size-1),j)] or\
                                   0 in [grid[x][j] for x in range(i-(size-1),i)]):
                                    #check whether is stair, stair instances all in list s:

                                    
                                    s2 = []
                                    I = i
                                    J = j
                                    I1 = i
                                    J1 = j
                                    for x2 in range(I,I+height,size-1):
                                        for y2 in range(J+1,J+size):
                                            if x2 < int(dim) and y2 < int(dim):
                                                s2.append(grid[x2][y2])
                                        J += size-1
                                    for y3 in range(J1+(size-1),J1+(width-1),size-1):
                                        for x3 in range(I1+1,I1+size):
                                            if x3 < int(dim) and y3 < int(dim):
                                                s2.append(grid[x3][y3])
                                        I1 += size-1
                                    if 0 not in s2:
                                        #print(i,j)
                                        stairs +=1 
    




                                
                                   
                            elif j > int((dim-1)-(width-1)-(size-1)) and (i >= size-1) and (i <= int((dim-1)-(height-1)-(size-1))):
                                #check
                                if (0 in [grid[i-(size-1)][y] for y in range(j-(size-1),j)] or\
                                   0 in [grid[x][j] for x in range(i-(size-1),i)]):
                                    #check whether is stair

                                    
                                    s3 = []
                                    I = i
                                    J = j
                                    I1 = i
                                    J1 = j
                                    for x2 in range(I,I+height,size-1):
                                        for y2 in range(J+1,J+size):
                                            if x2 < int(dim) and y2 < int(dim):
                                                s3.append(grid[x2][y2])
                                        J += size-1
                                    for y3 in range(J1+(size-1),J1+(width-1),size-1):
                                        for x3 in range(I1+1,I1+size):
                                            if x3 < int(dim) and y3 < int(dim):
                                                s3.append(grid[x3][y3])
                                        I1 += size-1
                                    if 0 not in s3:
                                        #print(i,j)
                                        stairs +=1 
    
    





                                
   
#don't need check
                            else:
                                #check whether is stair
                               
                                s4 = []
                                I = i
                                J = j
                                I1 = i
                                J1 = j
                                for x2 in range(I,I+height,size-1):
                                    for y2 in range(J+1,J+size):
                                        if x2 < int(dim) and y2 < int(dim):
                                            s4.append(grid[x2][y2])
                                    J += size-1
                                for y3 in range(J1+(size-1),J1+(width-1),size-1):
                                    for x3 in range(I1+1,I1+size):
                                        if x3 < int(dim) and y3 < int(dim):
                                            s4.append(grid[x3][y3])
                                    I1 += size-1
                                if 0 not in s4:
                                    #print(i,j)
                                    stairs +=1 
                                                                 

            if stairs != 0:
                L.append((nb,stairs))
        if L != []:
            d[size] = L

    return d
    # Replace return {} above with your code
































# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are step sizes, and whose values are pairs of the form
# (number_of_steps, number_of_stairs_with_that_number_of_steps_of_that_step_size),
# ordered from smallest to largest number_of_steps.
stairs = stairs_in_grid()
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    for nb_of_steps, nb_of_stairs in stairs[step_size]:
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print(f'     {nb_of_stairs} {stair_or_stairs} with {nb_of_steps} {step_or_steps}')

