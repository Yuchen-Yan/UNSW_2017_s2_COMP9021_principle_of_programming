# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing the standard form
# decomposition of the permutation into cycles (see wikepedia page on permutations for details).
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix and in-place uses.
#
# Written by *** and Eric Martin for COMP9021


class PermutationError(Exception):
    def __init__(self, message):
        self.message = message

class Permutation:
    def __init__(self, *args, length = None):
        if args and length == None:
            for i in args:
                if not isinstance(i,int) or i <= 0:
                    raise PermutationError('Cannot generate permutation from these arguments')
            self.args = args
            self.length = len(args)
            self.nb_of_cycles = None
        elif length != None and not args:
            if length <= 0:
                raise PermutationError('Cannot generate permutation from these arguments')
            else:
                self.length = length
                self.args = tuple(range(1,self.length+1))
                self.nb_of_cycles = None
        elif args and length != None:
            for i in args:
                if not isinstance(i,int) or i <= 0:
                    raise PermutationError('Cannot generate permutation from these arguments')
            if length <= 0:
                raise PermutationError('Cannot generate permutation from these arguments')
            if len(args) != length:
                raise PermutationError('Cannot generate permutation from these arguments')
            self.args = args
            self.length = length
            self.nb_of_cycles = None
        elif not args and length == None:
            self.args = ()
            self.length = 0
            self.nb_of_cycles = None

    def __len__(self):
        return self.length

    def __repr__(self):
        if self.args:
            return f'Permutation{self.args}'
        elif self.args == ():
            return 'Permutation()'



    def __str__(self):
        if self.args == ():
            self.nb_of_cycles = 0
            return '()'
        else:
            perm = list(self.args)
            dic = {i+1: perm[i] for i in range(len(perm))}
            permus = []

        while dic:
            first = next(iter(dic)) # arbitrary starting element
            current = dic[first]
            next_e = dic[current]
            permu = []
            Flag = True
            while Flag:
                permu.append(current)
                del dic[current]
                current = next_e
                if next_e in dic:
                    next_e = dic[next_e]
                else:
                    Flag = False
            permus.append(permu)
#Sort each cycles, which inside each cycle begain with the largest.
#Between each cycles the first number from smallest to largest           
        cycles1 = []
        for i in permus:
            f = max(i)
            if len(i) == 1:
                pass
            else:
                i = tuple(i[i.index(f):]+i[:i.index(f)])
            cycles1.append(i)
        cycles1 = sorted(cycles1, key  = lambda d:d[0], reverse = False)
#Change each list of cycles into string       
        cycles2 = []
        for item in cycles1:
            string = '('
            for j in item[:-1]:
                string += f'{j} '
            string += f'{item[-1]})'
            cycles2.append(string)
#Combine each cycle into one string        
        out_string = ''
        for i in cycles2:
            out_string += f'{i}'
        self.nb_of_cycles = len(cycles2)
        return out_string
        
                


        


    def __mul__(self, permutation):
        if self.length != permutation.length:
            raise PermutationError('Cannot compose permutations of different lengths')
        elif permutation.length == 0:
            return Permutation()
        else:
            s = []
            for i in range(len(self.args)):
                s.append(permutation.args[self.args[i]-1])
            s = tuple(s)
            return Permutation(*s)             

    def __imul__(self, permutation):

        if self.length != permutation.length:
            raise PermutationError('Cannot compose permutations of different lengths')
        elif permutation.length == 0:
            return Permutation()
        else:
            s1 = []
            for i in range(len(permutation.args)):
                s1.append(permutation.args[self.args[i]-1])
            s1 = tuple(s1)
        return Permutation(*s1)

    def inverse(self):
        if self.length == 0:
            return Permutation()
        else:
            s = []
            for i in range(1, self.length+1):
                s.append(self.args.index(i)+1)
            s = tuple(s)
            return Permutation(*s)
    # Insert your code for helper functions, if needed



        

