# Generates a binary tree T whose shape is random and whose nodes store
# random even positive integers, both random processes being directed by user input.
# With M being the maximum sum of the nodes along one of T's branches, minimally expands T
# to a tree T* such that:
# - every inner node in T* has two children, and
# - the sum of the nodes along all of T*'s branches is equal to M.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

from binary_tree_adt import *


def create_tree(tree, for_growth, bound):
    if randrange(max(for_growth, 1)):
        tree.value = 2 * randrange(bound + 1)
        tree.left_node = BinaryTree()
        tree.right_node = BinaryTree()
        create_tree(tree.left_node, for_growth - 1, bound)
        create_tree(tree.right_node, for_growth - 1, bound)


def expand_tree(tree):
    m = all_path(tree)
    expand(tree, m)



def all_path(tree):
    path_sum = 0
    res = []
    _all_path(tree, path_sum, res)
    return max(res)

def _all_path(tree, path_sum, res):
    if tree.left_node.value is None and tree.right_node.value is None:
        path_sum += tree.value
        res.append(path_sum)
    elif tree.left_node.value is None or tree.right_node.value is None:
        path_sum += tree.value
        res.append(path_sum)
    else:
        path_sum += tree.value
        
    if tree.left_node.value is not None:
        _all_path(tree.left_node, path_sum, res)
    if tree.right_node.value is not None:
        _all_path(tree.right_node, path_sum, res)
        

def expand(tree, m):
    the_sum = 0
    _expand(tree, m, the_sum)

def _expand(tree, m, the_sum):
    l_flag = True
    r_flag = True
    if tree.left_node.value is None and tree.right_node.value is None:
        the_sum += tree.value
        if m == the_sum:
            l_flag = False
            r_flag = False
            pass
        else:
            tree.left_node = BinaryTree(m-the_sum)
            tree.right_node = BinaryTree(m-the_sum)
            l_flag = False
            r_flag = False
            
    elif tree.left_node.value is None and tree.right_node.value is not None: 
        the_sum += tree.value
        if m == the_sum:
            l_flag = False
            pass
        else:
            tree.left_node = BinaryTree(m-the_sum)
            l_flag = False
            
    elif tree.left_node.value is not None and tree.right_node.value is None:
        the_sum += tree.value
        if m == the_sum:
            r_flag = False
            pass
        else:
            tree.right_node = BinaryTree(m-the_sum)
            r_flag = False
            
    else:
        the_sum += tree.value

    if tree.left_node.value is not None and l_flag:
        _expand(tree.left_node, m, the_sum)
    if tree.right_node.value is not None and r_flag:
        _expand(tree.right_node, m, the_sum)
        
    


# Possibly define other functions

                
try:
    for_seed, for_growth, bound = [int(x) for x in input('Enter three positive integers: ').split()
                                   ]
    if for_seed < 0 or for_growth < 0 or bound < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
 
seed(for_seed)
tree = BinaryTree()
create_tree(tree, for_growth, bound)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
expand_tree(tree)
print('Here is the expanded tree:')
tree.print_binary_tree()



