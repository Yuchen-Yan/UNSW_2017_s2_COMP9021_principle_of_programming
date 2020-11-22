# Randomly fills a grid of size height and width whose values are input by the user,
# with nonnegative integers randomly generated up to an upper bound N also input the user,
# and computes, for each n <= N, the number of paths consisting of all integers from 1 up to n
# that cannot be extended to n+1.
# Outputs the number of such paths, when at least one exists.
#
# Written by Yuchen Yan and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))




        

def get_paths():
    path = defaultdict()
    for i in range(height):
        for j in range(width):
            if grid[i][j] != 1:
                continue
            find_next(i,j,1,path)

    return path

    
    # Replace pass above with your code

# Insert your code for other functions
def find_next(i,j,v,path):
    v += 1
    if 0 < i < height-1 and 0 < j < width-1: 
        if grid[i-1][j] != v and grid[i+1][j] != v and grid[i][j-1] != v and grid[i][j+1] != v:
            if path.__contains__(v-1):
                path[v-1] += 1
            else:
                path[v-1] = 1
        else:    
            if grid[i-1][j] == v:
                find_next(i-1,j,v,path)
            if grid[i+1][j] == v:
                find_next(i+1,j,v,path)
            if grid[i][j-1] == v:
                find_next(i,j-1,v,path)
            if grid[i][j+1] == v:
                find_next(i,j+1,v,path)

                
    elif i == 0 and j == 0:
        if  grid[i+1][j] != v  and grid[i][j+1] != v:
            if path.__contains__(v-1):
                path[v-1] += 1
            else:
                path[v-1] = 1
        else:    
            if grid[i+1][j] == v:
                find_next(i+1,j,v,path)
            if grid[i][j+1] == v:
                find_next(i,j+1,v,path)

                
    elif i == 0 and j == width - 1:
        if  grid[i+1][j] != v and grid[i][j-1] != v:
            if path.__contains__(v-1):
                path[v-1] += 1
            else:
                path[v-1] = 1
        else:    
            if grid[i+1][j] == v:
                find_next(i+1,j,v,path)
            if grid[i][j-1] == v:
                find_next(i,j-1,v,path)
 
                
    elif i == height-1 and j == 0:
        if grid[i-1][j] != v and  grid[i][j+1] != v:
            if path.__contains__(v-1):
                path[v-1] += 1
            else:
                path[v-1] = 1
        else:    
            if grid[i-1][j] == v:
                find_next(i-1,j,v,path)
            if grid[i][j+1] == v:
                find_next(i,j+1,v,path)

                
    elif i == height-1 and j == width-1:
        if grid[i-1][j] != v and grid[i][j-1] != v:
            if path.__contains__(v-1):
                path[v-1] += 1
            else:
                path[v-1] = 1
        else:    
            if grid[i-1][j] == v:
                find_next(i-1,j,v,path)
            if grid[i][j-1] == v:
                find_next(i,j-1,v,path)
 
                
    elif i == 0:
        if grid[i+1][j] != v and grid[i][j-1] != v and grid[i][j+1] != v:
            if path.__contains__(v-1):
                path[v-1] += 1
            else:
                path[v-1] = 1
        else:    
            if grid[i+1][j] == v:
                find_next(i+1,j,v,path)
            if grid[i][j-1] == v:
                find_next(i,j-1,v,path)
            if grid[i][j+1] == v:
                find_next(i,j+1,v,path)

                
    elif i == height-1:
        if grid[i-1][j] != v  and grid[i][j-1] != v and grid[i][j+1] != v:
            if path.__contains__(v-1):
                path[v-1] += 1
            else:
                path[v-1] = 1
        else:    
            if grid[i-1][j] == v:
                find_next(i-1,j,v,path)
            if grid[i][j-1] == v:
                find_next(i,j-1,v,path)
            if grid[i][j+1] == v:
                find_next(i,j+1,v,path)

                
    elif j == 0:
        if grid[i-1][j] != v and grid[i+1][j] != v and grid[i][j+1] != v:
            if path.__contains__(v-1):
                path[v-1] += 1
            else:
                path[v-1] = 1
        else:    
            if grid[i-1][j] == v:
                find_next(i-1,j,v,path)
            if grid[i+1][j] == v:
                find_next(i+1,j,v,path)
            if grid[i][j+1] == v:
                find_next(i,j+1,v,path)

                
    elif j == width-1:
        if grid[i-1][j] != v and grid[i+1][j] != v and grid[i][j-1] != v:
            if path.__contains__(v-1):
                path[v-1] += 1
            else:
                path[v-1] = 1
        else:    
            if grid[i-1][j] == v:
                find_next(i-1,j,v,path)
            if grid[i+1][j] == v:
                find_next(i+1,j,v,path)
            if grid[i][j-1] == v:
                find_next(i,j-1,v,path)
 
        
        
    

















    
try:
    for_seed, max_length, height, width = [int(i) for i in
                                                  input('Enter four nonnegative integers: ').split()
                                       ]
    if for_seed < 0 or max_length < 0 or height < 0 or width < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, max_length) for _ in range(width)] for _ in range(height)]
print('Here is the grid that has been generated:')
display_grid()
paths = get_paths()
if paths:
    for length in sorted(paths):
        print(f'The number of paths from 1 to {length} is: {paths[length]}')

