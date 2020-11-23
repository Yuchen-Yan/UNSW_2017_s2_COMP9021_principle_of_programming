from itertools import permutations

L = []
for i in range(10,100):
    L.append(i)

L_1 = list(permutations(L,3))
a = []

for i in range(len(L_1)):
    answer = sorted(list(str(L_1[i][0] * L_1[i][1] * L_1[i][2])))
    digit = sorted(list(str(L_1[i][0]))+list(str(L_1[i][1]))+list(str(L_1[i][2])))
    answer = list(set(answer))
    digit = list(set(digit))
    
    if answer == digit and len(digit) == 6:
        an = sorted([L_1[i][0],L_1[i][1],L_1[i][2]])
        if an not in a:
            a.append(an)
        

for i in range(len(a)):
    print(f'{a[i][0]} x {a[i][1]} x {a[i][2]} = {a[i][0]*a[i][1]*a[i][2]}', end = '\n')
