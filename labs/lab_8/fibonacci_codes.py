
def encode(n):
    '''
    Retuns the Fibonacci code of n, meant to be a strictly positive integer.
    
    >>> encode(1)
    '11'
    >>> encode(2)
    '011'
    >>> encode(3)
    '0011'
    >>> encode(4)
    '1011'
    >>> encode(5)
    '00011'
    >>> encode(6)
    '10011'
    >>> encode(7)
    '01011'
    >>> encode(8)
    '000011'
    >>> encode(9)
    '100011'
    >>> encode(10)
    '010011'
    >>> encode(11)
    '001011'
    >>> encode(12)
    '101011'
    >>> encode(13)
    '0000011'
    >>> encode(14)
    '1000011'
    
    '''
    numbers = fibonacci_up_to_n(n)
    bits = ['0'] * len(numbers) + ['1']
    reminder = n
    for i in range(len(numbers) - 1, -len(numbers), -1):
        if reminder == 0:
            break
        if reminder >= numbers[i]:
            reminder -= numbers[i]
            bits[i] = '1'
    return ''.join(bits)



def decode(code):
    '''
    The argument is meant to be a string of 0's and 1's.
    Returns 0 if the argument cannot be a Fibonacci code;
    otherwise returns the integer argument is the Fibonacci code of.
    
    >>> decode('1')
    0
    >>> decode('01')
    0
    >>> decode('111')
    0
    >>> decode('100011011')
    0
    >>> decode('11')
    1
    >>> decode('011')
    2
    >>> decode('0011')
    3
    >>> decode('1011')
    4
    >>> decode('00011')
    5
    >>> decode('10011')
    6
    >>> decode('01011')
    7
    >>> decode('000011')
    8
    >>> decode('100011')
    9
    >>> decode('010011')
    10
    >>> decode('001011')
    11
    >>> decode('101011')
    12
    >>> decode('0000011')
    13
    >>> decode('1000011')
    14
    
    '''
    if len(code) < 2 or code[-2:] != '11':
        return 0
    previous_bit_set = False
    previous = 1
    current = 1
    n = 0
    for bit in (int(c) for c in code[:-1]):
        if bit:
            if previous_bit_set:
                return 0
            previous_bit_set = True
            n += current
            
        else:
            previous_bit_set = False
            
        current, previous = previous+current, current
    return n

def fibonacci_up_to_n(n):
    previous = 1
    current = 1
    numbers = []
    while current <= n:
        numbers.append(current)
        current, previous = previous+current, current
    return numbers


   
if __name__ == '__main__':
    import doctest
    doctest.testmod()
