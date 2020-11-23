def merging(string1,string2,string3):
    if len(string1) ==0 and string2 == string3:
        return True
    if len(string2) ==0 and string1 == string3:
        return True
    if len(string1) == 0 and len(string2) == 0:
        return False
    
    if string1[0] == string3[0] and merging(string1[1:], string2, string3[1:]):
        return True
    if string2[0] == string3[0] and merging(string1, string2[1:], string3[1:]):
        return True
    return False


ranks = 'first','second','third'
strings = [input(f'Please input the {rank} string: ') for rank in ranks]

last = 0
if len(strings[0]) < len(strings[1]):
    last = 1
if len(strings[last]) < len(strings[2]):
    last = 2

if last == 0:
    first,second = 1,2
elif last == 1:
    first, second = 0,2
elif last == 2:
    first, second = 0,1

if len(strings[first]) + len(strings[second]) == len(strings[last]) and merging(strings[first], strings[second], strings[last]):
    print(f'The {ranks[last]} string can be obtained by merging the other two.')
else:
    print('No solution')
