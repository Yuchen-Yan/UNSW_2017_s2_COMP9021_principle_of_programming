
from math import sqrt

L = [0]*1000


for i in range(100,999):
    for j in range(i//2+1):
        a = sqrt(j)
        b = sqrt(i-j)
        if a - int(sqrt(j)) == 0 and b - int(sqrt(i-j)) == 0:
            L[i] = (int(a),int(b))
            break


L_1 = []
L_2 = []
for i in range(100,999):
    if L[i] != 0 and L[i+1] != 0 and L[i+2] != 0:
        L_1.append((L[i],L[i+1],L[i+2]))
        L_2.append((i,i+1,i+2))
#print(L_1)



for i in range(len(L_1)):
    print(f'{L_2[i]} (equal to ({L_1[i][0][0]}^2+{L_1[i][0][1]}^2,{L_1[i][1][0]}^2+{L_1[i][1][1]}^2,{L_1[i][2][0]}^2+{L_1[i][2][1]}^2)) is a solution.', end = '\n')

