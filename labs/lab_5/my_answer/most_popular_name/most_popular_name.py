#This is wrriten by Yuchen Yan for comp9021 lab5

'''
This program is aim to find the most popular year in terms of a given name
'''



import os
import sys
from collections import defaultdict

i_name = input('Enter a first name: ')



o_d = 'names'
dic_m = dict()
dic_f = dict()

for filename in os.listdir(o_d):
    if not filename.endswith('.txt'):
        continue



    
    with open(o_d+'/'+filename) as names:
        sum_f = 0
        sum_m = 0
        info_f = dict()
        info_m = dict()



        
        for line in names:
            name, gender, frequent = line.split(',')
            if gender == 'F':
                frequent = int(frequent.rstrip('\n'))
                info_f[name] = frequent
                sum_f += frequent
            else:
                frequent = int(frequent.rstrip('\n'))
                info_m[name] = frequent
                sum_m += frequent
 #       info_f = sorted(info_f, key = lambda l:l[1], reverse = True)
 #       info_m = sorted(info_m, key = lambda l:l[1], reverse = True)

        if info_f.__contains__(i_name):
            p_f = info_f[i_name]/sum_f*100
            dic_f[filename[3:7]] = p_f
        if info_m.__contains__(i_name):
            p_m = info_m[i_name]/sum_m*100
            dic_m[filename[3:7]] = p_m


dic_f = sorted(dic_f.items(), key = lambda item:item[1], reverse = False)
dic_m = sorted(dic_m.items(), key = lambda item:item[1], reverse = False)

if len(dic_f) == 0 and len(dic_m) == 0:
    print('In all years,', i_name,'was never given as a female name.')
    print('In all years,', i_name,'was never given as a female name.')
elif len(dic_f) != 0 and len(dic_m) == 0:
    print('In terms of frequency,', i_name,'was the most popular as a female name first in the year ',dic_f[0][0],'.')
    print(f'  It then accounted for {dic_f[0][1]:.2f}% of all female names')
    print('In all years,', i_name ,'was never given as a female name.')
elif len(dic_f) == 0 and len(dic_m) != 0:
    print('In all years,', i_name ,'was never given as a female name.')
    print('In terms of frequency,', i_name,'was the most popular as a male name first in the year ',dic_m[0][0],'.')
    print(f'  It then accounted for {dic_m[0][1]:.2f}% of all male names')
else:
    print('In terms of frequency,', i_name,'was the most popular as a female name first in the year ',dic_f[0][0],'.')
    print(f'  It then accounted for {dic_f[0][1]:.2f}% of all female names')
    print('In terms of frequency,', i_name,'was the most popular as a male name first in the year ',dic_m[0][0],'.')
    print(f'  It then accounted for {dic_m[0][1]:.2f}% of all male names')

    
            























