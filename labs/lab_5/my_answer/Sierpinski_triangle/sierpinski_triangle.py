#This is written by Yuchen Yan 
'''
this program is aim to solve the sierpinski trangle problam
'''



file_name = 'sierpinski_triangle.tex'

with open(file_name, 'w') as file:
    file.write('\\documentclass[10pt]{article}\n')
    file.write('\\usepackage{tikz}\n')
    file.write('\\pagestyle{empty}\n\n')
    file.write('\\begin{document}\n\n')
    file.write('\\vspace*{\\fill}\n')
    file.write('\\begin{center}\n')
    file.write('\\begin{tikzpicture}[scale=0.047]\n\n')

    T1 = []

    x=0
    y=0
    L = []
    for i in range(1,128+1):
        T = []

        x1 = x
        y1 = y
        for j in range(i):
            if j == 0:
                T.append(1)
                L.append((x1,y1))
            elif j == i-1:
                T.append(1)
                L.append((x1,y1))
            else:
                current = T1[j-1]+T1[j]
                T.append(current)
                if current%2 == 1:
                    L.append((x1,y1))
                
            
            x1 += 2
            
        T1 = T
        
        x -= 1
        y -= 2

    for i in range(len(L)):
        a = L[i][0]
        b = L[i][1]
        file.write(f'\\fill({a},{b}) rectangle({a+2},{b+2});\n')
    file.write('\\end{tikzpicture}\n')
    file.write('\\end{center}\n')
    file.write('\\vspace*{\\fill}\n\n')
    file.write('\\end{document}\n')



    









