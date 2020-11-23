#This is writen by Yuchen Yan
'''
This program is aim to solve the evaluatee to 100 problem
'''

L = ['','+','-']




for i in range(3**8-1):
  
    operator = [L[i%3],L[int((i/3)%3)],L[int((i/(3**2))%3)],L[int((i/(3**3))%3)],L[int((i/(3**4))%3)],L[int((i/(3**5))%3)],L[int((i/(3**6))%3)],L[int((i/(3**7))%3)]]



                
    if eval('1'+operator[0]+'2'+operator[1]+'3'+operator[2]+'4'+operator[3]+'5'+operator[4]+'6'+operator[5]+'7'+operator[6]+'8'+operator[7]+'9')==100:
        v = 1
        print(v, end = '')
        for j in range(8):
            v += 1
            if operator[j] != '':
                print(' ', operator[j],' ', end = '')
            print(v, end = '')
            
        print(' = 100')
        #print(f'1{operator[0]}2{operator[1]}3{operator[2]}4{operator[3]}5{operator[4]}6{operator[5]}7{operator[6]}8{operator[7]}9=100')

                
    elif eval('-1'+operator[0]+'2'+operator[1]+'3'+operator[2]+'4'+operator[3]+'5'+operator[4]+'6'+operator[5]+'7'+operator[6]+'8'+operator[7]+'9')==100:
        v = 1
        print('-',v, end = '')
        for j in range(8):
            v += 1
            if operator[j] != '':
                print(' ', operator[j],' ', end = '')
            print(v, end = '')
        print(' = 100')
'''

                
    #if eval('1'+operator[0]+'2'+operator[1]+'3'+operator[2]+'4'+operator[3]+'5'+operator[4]+'6'+operator[5]+'7'+operator[6]+'8'+operator[7]+'9')==100:
    value = eval('1'+operator[0]+'2'+operator[1]+'3'+operator[2]+'4'+operator[3]+'5'+operator[4]+'6'+operator[5]+'7'+operator[6]+'8'+operator[7]+'9') 
    if value == 100:
        print(f'1{operator[0]}2{operator[1]}3{operator[2]}4{operator[3]}5{operator[4]}6{operator[5]}7{operator[6]}8{operator[7]}9=100')

                
    #elif eval('-1'+operator[0]+'2'+operator[1]+'3'+operator[2]+'4'+operator[3]+'5'+operator[4]+'6'+operator[5]+'7'+operator[6]+'8'+operator[7]+'9')==100:
    value1 = eval('-'+'1'+operator[0]+'2'+operator[1]+'3'+operator[2]+'4'+operator[3]+'5'+operator[4]+'6'+operator[5]+'7'+operator[6]+'8'+operator[7]+'9')
    if value1 == 100:
        print(f'-1{operator[0]}2{operator[1]}3{operator[2]}4{operator[3]}5{operator[4]}6{operator[5]}7{operator[6]}8{operator[7]}9=100')
    
'''
