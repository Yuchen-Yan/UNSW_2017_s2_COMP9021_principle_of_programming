#This is writtrn bu Yuchen Yan for lab5

'''
This program is aim to check the nine puzzle and solve the nine puzzle problem 
'''



def validate_9_puzzle(grid):
    if len(grid) == 3 and len(grid[0])==3 and len(grid[1])==3 and len(grid[2])==3:
        s = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                s.add(grid[i][j])
        if len(s) != 9:
            print('This is an invalid or unsolvable 9 puzzle')
            return
        for i in range(0,9):
            if i not in s:
                print('This is an invalid or unsolvable 9 puzzle')
                return         
        print('This is a valid 9 puzzle, and it is solvable')
    else:
        print('This is an invalid or unsolvable 9 puzzle')
        return

def solve_9_puzzle(grid):

'''
grid = [[2,1,3],[4,5,6],[7,8,0]]
grid1 = [[1,3],[1,2,3],[2,3,4]]

print('For grid 1:')
validate_9_puzzle(grid)
print('For grid 2')
validate_9_puzzle(grid1)
'''    
