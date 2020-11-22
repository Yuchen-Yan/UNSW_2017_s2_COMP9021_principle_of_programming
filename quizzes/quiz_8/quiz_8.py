# Randomly fills a grid of size 10 x 10 with digits between 0
# and bound - 1, with bound provided by the user.
# Given a point P of coordinates (x, y) and an integer "target"
# also all provided by the user, finds a path starting from P,
# moving either horizontally or vertically, in either direction,
# so that the numbers in the visited cells add up to "target".
# The grid is explored in a depth-first manner, first trying to move north,
# always trying to keep the current direction,
# and if that does not work turning in a clockwise manner.
#
# Written by Eric Martin for COMP9021


import sys
from random import seed, randrange
from collections import defaultdict

from stack_adt import *



def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def explore_depth_first(x, y, target):
    visited = defaultdict(list)
    sums = 0 
    path = []
    visited[(x,y)]
    sums += grid[x][y]
    
    if sums == target:
        return [(x,y)]
    if sums > target:
        return None

    operation = [(-1,0), (0,1), (1,0), (0,-1)]
    op = 0
    path.append((x,y))
    while sums != target:
        if len(visited) == 100:
            print(sums)
            return None
        if visited[(x,y)] != 4:            
            if x + operation[op][0]< 0 or x + operation[op][0]> 9 \
               or y + operation[op][1]< 0 or y + operation[op][1]> 9\
               or(sums + grid[x + operation[op][0]][y + operation[op][1]]) > target\
               or (x + operation[op][0],y + operation[op][1]) in visited:
                visited[(x,y)].append(operation[op])
                if len(visited[(x,y)]) == 4:
                    path.pop()
                    sums -= grid[x][y]
                    visited.pop((x,y))
                    x, y = path[-1][0], path[-1][1]
                    op = (op+2)%4
                    continue
                op = (op+1)%4
                continue
            else:
                x += operation[op][0]
                y += operation[op][1]
                sums += grid[x][y]
                path.append((x,y))
                visited[(x,y)]
        else:
                path.pop()
                sums -= grid[x][y]
                visited.pop((x,y))
                x, y = path[-1][0], path[-1][1]
                op = (op+1)%4
            
    
    return path








try:
    for_seed, bound, x, y, target = [int(x) for x in input('Enter five integers: ').split()]
    if bound < 1 or x not in range(10) or y not in range(10) or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(bound) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = explore_depth_first(x, y, target)
if not path:
    print(f'There is no way to get a sum of {target} starting from ({x}, {y})')
else:
    print('With North as initial direction, and exploring the space clockwise,')
    print(f'the path yielding a sum of {target} starting from ({x}, {y}) is:')
    print(path)
