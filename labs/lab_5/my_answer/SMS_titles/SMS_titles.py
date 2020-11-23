#This is written by Yuchen Yan for compo9021 lab5

'''

'''

import sys
import os.path
import bs4
import openpyxl
import re




file_name = ('SMH_title.txt')
if os.path.isfile(file_name):
    print('This file already exits.')
    print('Please give a new file name')
    sys.exit()



with open('SMH.html',encoding = 'utf-8') as file,\
     open(file_name, 'w') as write:
    soup = bs4.BeautifulSoup(file,'lxml')
    
    title = soup.findAll('a', attrs = {'href':re.compile('^http'), 'title':re.compile('.*')})
    
    for item in title:
        #print(item)
        item = item.get_text()
        write.write(f'{item}\n')
        


















    

