class SudokuError(Exception):
    def __init__(self, message):
        self.message = message

class Sudoku:
    def __init__(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.grid = []
            for line in file:
                if list(line.split()):
                    self.grid.append([int(i) for i in line if i.isdigit()])
            if len(self.grid) != 9:
                raise SudokuError('Incorrect input')
            for i in range(len(self.grid)):
                if len(self.grid[i]) != 9:
                    raise SudokuError('Incorrect input')

    def preassess(self):
        for line in self.grid:
            check = [i for i in line if i != 0]
            if len(check) != len(set(check)):
                print('There is clearly no solution.')
                return

        for i in range(len(self.grid)):
            check = [self.grid[j][i] for j in range(len(self.grid)) if self.grid[j][i] != 0]
            if len(check) != len(set(check)):
                print('There is clearly no solution.')
                return

        for i in 1,4,7:
            for j in 1,4,7:
                L = [self.grid[i-1][j-1],self.grid[i-1][j],self.grid[i-1][j+1],self.grid[i][j-1],self.grid[i][j],self.grid[i][j+1],self.grid[i+1][j-1],self.grid[i+1][j],self.grid[i+1][j+1]]
                check = [k for k in L if k != 0]                                
                if len(check) != len(set(check)):
                    print('There is clearly no solution.')
                    return
        print('There might be a solution.')
        return
    


    def bare_tex_output(self):
        name = self.filename[:-4]+'_bare.tex'
        with open(name,'w') as file:
            print('\\documentclass[10pt]{article}\n'
                  '\\usepackage[left=0pt,right=0pt]{geometry}\n'
                  '\\usepackage{tikz}\n'
                  '\\usetikzlibrary{positioning}\n'
                  '\\usepackage{cancel}\n'
                  '\\pagestyle{empty}\n'
                  '\n'
                  '\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n'
                  '                               label=above right:{\\tiny #2},\n'
                  '                               label=below left:{\\tiny #3},\n'
                  '                               label=below right:{\\tiny #4}]{#5};}}\n'
                  '\n'
                  '\\begin{document}\n'
                  '\n'
                  '\\tikzset{every node/.style={minimum size=.5cm}}\n'
                  '\n'
                  '\\begin{center}\n'
                  '\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline', file = file)
            for i in range(9):
                print(f'% Line {i+1}', file = file)
                for j in range(8):
                    if not (j+1)%3: 
                        if self.grid[i][j] == 0:
                            print('\\N{}{}{}{}{} &',file = file)
                        else:
                            print('\\N{}{}{}{}{%d} &'%(self.grid[i][j]),file = file)
                    else:
                        if self.grid[i][j] == 0:
                            print('\\N{}{}{}{}{} & ',file = file, end = '')
                        else:
                            print('\\N{}{}{}{}{%d} & '%(self.grid[i][j]),file = file, end = '')                                               
                if self.grid[i][8] == 0:
                    print('\\N{}{}{}{}{} \\', file = file, end = '')
                    print('\\ \\hline',file = file, end = '')
                else:
                    print('\\N{}{}{}{}{%d} \\'%(self.grid[i][8]), file = file, end = '')
                    print('\\ \\hline',file = file, end = '')
                if not (i+1) % 3:
                    print('\\hline', file = file, end = '')
                if i != 8:
                    print('\n', file = file)
                else:
                    print('', file = file)
            print('\\end{tabular}\n'
                  '\\end{center}\n'
                  '\n'
                  '\\end{document}', file = file)

            
    def forced_tex_output(self):
        while True:
            flag = True
            frequency = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if self.grid[i][j] != 0:
                        frequency[self.grid[i][j]] += 1
                        
            position = [[-1,-1], [-1,0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
            for _ in range(9):
                if frequency:
                    term = max(frequency, key = lambda x: frequency[x])
                    for i in 1,4,7:
                        for j in 1,4,7:
                            if term in [self.grid[i-1][j-1],self.grid[i-1][j],self.grid[i-1][j+1],\
                                       self.grid[i][j-1],  self.grid[i][j],  self.grid[i][j+1],\
                                       self.grid[i+1][j-1],self.grid[i+1][j],self.grid[i+1][j+1]]:
                                continue
                            possible = []
                            for k in position:
                                if self.grid[i+k[0]][j+k[1]] != 0:
                                    continue
                                if term in [self.grid[i+k[0]][0],self.grid[i+k[0]][1],self.grid[i+k[0]][2],\
                                           self.grid[i+k[0]][3],self.grid[i+k[0]][4],self.grid[i+k[0]][5],\
                                           self.grid[i+k[0]][6],self.grid[i+k[0]][7],self.grid[i+k[0]][8]]:
                                    continue
                                if term in [self.grid[0][j+k[1]],self.grid[1][j+k[1]],self.grid[2][j+k[1]],\
                                           self.grid[3][j+k[1]],self.grid[4][j+k[1]],self.grid[5][j+k[1]],\
                                           self.grid[6][j+k[1]],self.grid[7][j+k[1]],self.grid[8][j+k[1]]]:
                                    continue
                                possible.append(k)
                            if len(possible) == 1:
                                flag = False
                                self.grid[i+possible[0][0]][j+possible[0][1]] = term                        
                frequency.pop(term)
            if flag:
                break
        
        
        name = self.filename[:-4]+'_forced.tex'
        with open(name,'w') as file:
            print('\\documentclass[10pt]{article}\n'
                  '\\usepackage[left=0pt,right=0pt]{geometry}\n'
                  '\\usepackage{tikz}\n'
                  '\\usetikzlibrary{positioning}\n'
                  '\\usepackage{cancel}\n'
                  '\\pagestyle{empty}\n'
                  '\n'
                  '\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n'
                  '                               label=above right:{\\tiny #2},\n'
                  '                               label=below left:{\\tiny #3},\n'
                  '                               label=below right:{\\tiny #4}]{#5};}}\n'
                  '\n'
                  '\\begin{document}\n'
                  '\n'
                  '\\tikzset{every node/.style={minimum size=.5cm}}\n'
                  '\n'
                  '\\begin{center}\n'
                  '\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline', file = file)
            for i in range(9):
                print(f'% Line {i+1}', file = file)
                for j in range(8):
                    if not (j+1)%3: 
                        if self.grid[i][j] == 0:
                            print('\\N{}{}{}{}{} &',file = file)
                        else:
                            print('\\N{}{}{}{}{%d} &'%(self.grid[i][j]),file = file)
                    else:
                        if self.grid[i][j] == 0:
                            print('\\N{}{}{}{}{} & ',file = file, end = '')
                        else:
                            print('\\N{}{}{}{}{%d} & '%(self.grid[i][j]),file = file, end = '')                                               
                if self.grid[i][8] == 0:
                    print('\\N{}{}{}{}{} \\', file = file, end = '')
                    print('\\ \\hline',file = file, end = '')
                else:
                    print('\\N{}{}{}{}{%d} \\'%(self.grid[i][8]), file = file, end = '')
                    print('\\ \\hline',file = file, end = '')
                if not (i+1) % 3:
                    print('\\hline', file = file, end = '')
                if i != 8:
                    print('\n', file = file)
                else:
                    print('', file = file)
            print('\\end{tabular}\n'
                  '\\end{center}\n'
                  '\n'
                  '\\end{document}', file = file)



    def marked_tex_output(self):
        while True:
            flag = True
            frequency = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if self.grid[i][j] != 0:
                        frequency[self.grid[i][j]] += 1
                        
            position = [[-1,-1], [-1,0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
            for _ in range(9):
                if frequency:
                    term = max(frequency, key = lambda x: frequency[x])
                    for i in 1,4,7:
                        for j in 1,4,7:
                            if term in [self.grid[i-1][j-1],self.grid[i-1][j],self.grid[i-1][j+1],\
                                       self.grid[i][j-1],  self.grid[i][j],  self.grid[i][j+1],\
                                       self.grid[i+1][j-1],self.grid[i+1][j],self.grid[i+1][j+1]]:
                                continue
                            possible = []
                            for k in position:
                                if self.grid[i+k[0]][j+k[1]] != 0:
                                    continue
                                if term in [self.grid[i+k[0]][0],self.grid[i+k[0]][1],self.grid[i+k[0]][2],\
                                           self.grid[i+k[0]][3],self.grid[i+k[0]][4],self.grid[i+k[0]][5],\
                                           self.grid[i+k[0]][6],self.grid[i+k[0]][7],self.grid[i+k[0]][8]]:
                                    continue
                                if term in [self.grid[0][j+k[1]],self.grid[1][j+k[1]],self.grid[2][j+k[1]],\
                                           self.grid[3][j+k[1]],self.grid[4][j+k[1]],self.grid[5][j+k[1]],\
                                           self.grid[6][j+k[1]],self.grid[7][j+k[1]],self.grid[8][j+k[1]]]:
                                    continue
                                possible.append(k)
                            if len(possible) == 1:
                                flag = False
                                self.grid[i+possible[0][0]][j+possible[0][1]] = term                        
                frequency.pop(term)
            if flag:
                break
        position = [[-1,-1], [-1,0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
        for i in 1,4,7:
            for j in 1,4,7:
                for k in position:
                    terms = [1,2,3,4,5,6,7,8,9]
                    for x in [self.grid[i-1][j-1],self.grid[i-1][j],self.grid[i-1][j+1],\
                              self.grid[i][j-1],  self.grid[i][j],  self.grid[i][j+1],\
                              self.grid[i+1][j-1],self.grid[i+1][j],self.grid[i+1][j+1]]:
                        if x in terms:
                            terms.remove(x)
                    
                
                    if self.grid[i+k[0]][j+k[1]] == 0:
                        for z in range(9):
                            if self.grid[i+k[0]][z] in terms:
                                terms.remove(self.grid[i+k[0]][z])
                            if self.grid[z][j+k[1]] in terms:
                                terms.remove(self.grid[z][j+k[1]])
                        self.grid[i+k[0]][j+k[1]] = terms


            
        name = self.filename[:-4]+'_marked.tex'
        with open(name,'w') as file:
            print('\\documentclass[10pt]{article}\n'
                  '\\usepackage[left=0pt,right=0pt]{geometry}\n'
                  '\\usepackage{tikz}\n'
                  '\\usetikzlibrary{positioning}\n'
                  '\\usepackage{cancel}\n'
                  '\\pagestyle{empty}\n'
                  '\n'
                  '\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n'
                  '                               label=above right:{\\tiny #2},\n'
                  '                               label=below left:{\\tiny #3},\n'
                  '                               label=below right:{\\tiny #4}]{#5};}}\n'
                  '\n'
                  '\\begin{document}\n'
                  '\n'
                  '\\tikzset{every node/.style={minimum size=.5cm}}\n'
                  '\n'
                  '\\begin{center}\n'
                  '\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline', file = file)
            for i in range(9):
                print(f'% Line {i+1}', file = file)
                for j in range(8):
                    try:                            
                        int(self.grid[i][j])
                        if not (j+1)%3:
                            print('\\N{}{}{}{}{%d} &'%(self.grid[i][j]),file = file)
                        else:
                            print('\\N{}{}{}{}{%d} & '%(self.grid[i][j]),file = file,end = '')                           
                    except TypeError:
                        s12 = ''
                        s34 = ''
                        s56 = ''
                        s78 = ''
                        for k in self.grid[i][j]:
                            if k in [1,2]:
                                if s12 == '':
                                    s12 += str(k)
                                else:
                                    s12 += ' '+str(k)
                            elif k in [3,4]:
                                if s34 == '':
                                    s34 += str(k)
                                else:
                                    s34 += ' '+str(k)
                            elif k in [5,6]:
                                if s56 == '':
                                    s56 += str(k)
                                else:
                                    s56 += ' '+str(k)
                            elif k in [7,8,9]:
                                if s78 == '':
                                    s78 += str(k)
                                else:
                                    s78 += ' '+str(k)
                        if not (j+1)%3:
                            print('\\N{%s}{%s}{%s}{%s}{} &'%(s12,s34,s56,s78),file = file)
                        else:
                            print('\\N{%s}{%s}{%s}{%s}{} & '%(s12,s34,s56,s78),file = file, end = '')                           
                                
                        
                try:
                    int(self.grid[i][8])
                    print('\\N{}{}{}{}{%d} \\'%(self.grid[i][8]),file = file, end = '')
                    print('\\ \\hline',file = file, end = '')
                except TypeError:
                    s12 = ''
                    s34 = ''
                    s56 = ''
                    s78 = ''
                    for k in self.grid[i][8]:
                        if k in [1,2]:
                            if s12 == '':
                                s12 += str(k)
                            else:
                                s12 += ' '+str(k)
                        elif k in [3,4]:
                            if s34 == '':
                                s34 += str(k)
                            else:
                                s34 += ' '+str(k)
                        elif k in [5,6]:
                            if s56 == '':
                                s56 += str(k)
                            else:
                                s56 += ' '+str(k)
                        elif k in [7,8,9]:
                            if s78 == '':
                                s78 += str(k)
                            else:
                                s78 += ' '+str(k)
                    print('\\N{%s}{%s}{%s}{%s}{} \\'%(s12,s34,s56,s78),file = file, end = '')
                    print('\\ \\hline',file = file, end = '')

                if not (i+1) % 3:
                    print('\\hline', file = file, end = '')
                if i != 8:
                    print('\n', file = file)
                else:
                    print('', file = file)
            print('\\end{tabular}\n'
                  '\\end{center}\n'
                  '\n'
                  '\\end{document}', file = file)
            
                    
        
    
    def worked_tex_output(self):
        while True:
            flag = True
            frequency = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if self.grid[i][j] != 0:
                        frequency[self.grid[i][j]] += 1
                        
            position = [[-1,-1], [-1,0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
            for _ in range(9):
                if frequency:
                    term = max(frequency, key = lambda x: frequency[x])
                    for i in 1,4,7:
                        for j in 1,4,7:
                            if term in [self.grid[i-1][j-1],self.grid[i-1][j],self.grid[i-1][j+1],\
                                       self.grid[i][j-1],  self.grid[i][j],  self.grid[i][j+1],\
                                       self.grid[i+1][j-1],self.grid[i+1][j],self.grid[i+1][j+1]]:
                                continue
                            possible = []
                            for k in position:
                                if self.grid[i+k[0]][j+k[1]] != 0:
                                    continue
                                if term in [self.grid[i+k[0]][0],self.grid[i+k[0]][1],self.grid[i+k[0]][2],\
                                           self.grid[i+k[0]][3],self.grid[i+k[0]][4],self.grid[i+k[0]][5],\
                                           self.grid[i+k[0]][6],self.grid[i+k[0]][7],self.grid[i+k[0]][8]]:
                                    continue
                                if term in [self.grid[0][j+k[1]],self.grid[1][j+k[1]],self.grid[2][j+k[1]],\
                                           self.grid[3][j+k[1]],self.grid[4][j+k[1]],self.grid[5][j+k[1]],\
                                           self.grid[6][j+k[1]],self.grid[7][j+k[1]],self.grid[8][j+k[1]]]:
                                    continue
                                possible.append(k)
                            if len(possible) == 1:
                                flag = False
                                self.grid[i+possible[0][0]][j+possible[0][1]] = term                        
                frequency.pop(term)
            if flag:
                break
        position = [[-1,-1], [-1,0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
        for i in 1,4,7:
            for j in 1,4,7:
                for k in position:
                    terms = [1,2,3,4,5,6,7,8,9]
                    for x in [self.grid[i-1][j-1],self.grid[i-1][j],self.grid[i-1][j+1],\
                              self.grid[i][j-1],  self.grid[i][j],  self.grid[i][j+1],\
                              self.grid[i+1][j-1],self.grid[i+1][j],self.grid[i+1][j+1]]:
                        if x in terms:
                            terms.remove(x)
                    
                
                    if self.grid[i+k[0]][j+k[1]] == 0:
                        for z in range(9):
                            if self.grid[i+k[0]][z] in terms:
                                terms.remove(self.grid[i+k[0]][z])
                            if self.grid[z][j+k[1]] in terms:
                                terms.remove(self.grid[z][j+k[1]])
                        self.grid[i+k[0]][j+k[1]] = terms
                        

        
        name = self.filename[:-4]+'_worked.tex'
        with open(name,'w') as file:
            print('\\documentclass[10pt]{article}\n'
                  '\\usepackage[left=0pt,right=0pt]{geometry}\n'
                  '\\usepackage{tikz}\n'
                  '\\usetikzlibrary{positioning}\n'
                  '\\usepackage{cancel}\n'
                  '\\pagestyle{empty}\n'
                  '\n'
                  '\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n'
                  '                               label=above right:{\\tiny #2},\n'
                  '                               label=below left:{\\tiny #3},\n'
                  '                               label=below right:{\\tiny #4}]{#5};}}\n'
                  '\n'
                  '\\begin{document}\n'
                  '\n'
                  '\\tikzset{every node/.style={minimum size=.5cm}}\n'
                  '\n'
                  '\\begin{center}\n'
                  '\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline', file = file)
            for i in range(9):
                print(f'% Line {i+1}', file = file)
                for j in range(8):
                    try:                            
                        int(self.grid[i][j])
                        if not (j+1)%3:
                            print('\\N{}{}{}{}{%d} &'%(self.grid[i][j]),file = file)
                        else:
                            print('\\N{}{}{}{}{%d} & '%(self.grid[i][j]),file = file,end = '')                           
                    except TypeError:
                        s12 = ''
                        s34 = ''
                        s56 = ''
                        s78 = ''
                        for k in self.grid[i][j]:
                            if k in [1,2]:
                                if s12 == '':
                                    s12 += str(k)
                                else:
                                    s12 += ' '+str(k)
                            elif k in [3,4]:
                                if s34 == '':
                                    s34 += str(k)
                                else:
                                    s34 += ' '+str(k)
                            elif k in [5,6]:
                                if s56 == '':
                                    s56 += str(k)
                                else:
                                    s56 += ' '+str(k)
                            elif k in [7,8,9]:
                                if s78 == '':
                                    s78 += str(k)
                                else:
                                    s78 += ' '+str(k)
                        if not (j+1)%3:
                            print('\\N{%s}{%s}{%s}{%s}{} &'%(s12,s34,s56,s78),file = file)
                        else:
                            print('\\N{%s}{%s}{%s}{%s}{} & '%(s12,s34,s56,s78),file = file, end = '')                           
                                
                        
                try:
                    int(self.grid[i][8])
                    print('\\N{}{}{}{}{%d} \\'%(self.grid[i][8]),file = file, end = '')
                    print('\\ \\hline',file = file, end = '')
                except TypeError:
                    s12 = ''
                    s34 = ''
                    s56 = ''
                    s78 = ''
                    for k in self.grid[i][8]:
                        if k in [1,2]:
                            if s12 == '':
                                s12 += str(k)
                            else:
                                s12 += ' '+str(k)
                        elif k in [3,4]:
                            if s34 == '':
                                s34 += str(k)
                            else:
                                s34 += ' '+str(k)
                        elif k in [5,6]:
                            if s56 == '':
                                s56 += str(k)
                            else:
                                s56 += ' '+str(k)
                        elif k in [7,8,9]:
                            if s78 == '':
                                s78 += str(k)
                            else:
                                s78 += ' '+str(k)
                    print('\\N{%s}{%s}{%s}{%s}{} \\'%(s12,s34,s56,s78),file = file, end = '')
                    print('\\ \\hline',file = file, end = '')

                if not (i+1) % 3:
                    print('\\hline', file = file, end = '')
                if i != 8:
                    print('\n', file = file)
                else:
                    print('', file = file)
            print('\\end{tabular}\n'
                  '\\end{center}\n'
                  '\n'
                  '\\end{document}', file = file)                                           
                                            
                
                            

           
            












