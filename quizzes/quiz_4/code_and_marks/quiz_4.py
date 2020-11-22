# Uses data available at http://data.worldbank.org/indicator
# on Forest area (sq. km) and Agricultural land area (sq. km).
# Prompts the user for two distinct years between 1990 and 2004
# as well as for a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area has increased from oldest input year to most recent input year;
# - forest area has increased from oldest input year to most recent input year;
# - the ratio of increase in agricultural land area to increase in forest area determines
#   output order.

# Countries are output from those whose ratio is largest to those whose ratio is smallest.
# In the unlikely case where many countries share the same ratio, countries are output in
# lexicographic order.

# In case fewer than N countries are found, only that number of countries is output.


# Written by Yuchen Yan and Eric Martin for COMP9021


import sys
import os
import csv
from collections import defaultdict


agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
if not os.path.exists(agricultural_land_filename):
    print(f'No file named {agricultural_land_filename} in working directory, giving up...')
    sys.exit()
    
forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
if not os.path.exists(forest_filename):
    print(f'No file named {forest_filename} in working directory, giving up...')
    sys.exit()

    
try:
    years = {int(year) for year in
                           input('Input two distinct years in the range 1990 -- 2014: ').split('--')
            }
    if len(years) != 2 or any(year < 1990 or year > 2014 for year in years):
        raise ValueError
except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit()

    
try:
    top_n = int(input('Input a strictly positive integer: '))
    if top_n < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, giving up...')
    sys.exit()


countries = []
year_1, year_2 = None, None

# Insert your code here



dic = defaultdict(list)
dic_1 = defaultdict(list)
result = []
index_y = []
index_z = []


with open('API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv',encoding = 'utf-8') as agricultural,\
     open('API_AG.LND.FRST.K2_DS2_en_csv_v2.csv',encoding = 'utf-8') as forest:
    for index, line in enumerate(agricultural):
        if index ==4:
            L = line.split('","')
            L[0] = L[0][1:]
            for i, item in enumerate(L):
                if item.isdigit():
                    if int(item) in years:
                        index_y.append(i)
            year_1 = L[index_y[0]]
            year_2 = L[index_y[1]]
        elif index > 4:
            L = line.split('","')
            L[0] = L[0][1:]
            
            if L[index_y[1]] != '' and L[index_y[0]] != '':
                if float(L[index_y[1]]) > float(L[index_y[0]]):
                    dic[L[0]].append(float(L[index_y[1]])-float(L[index_y[0]]))
        

    for index, line in enumerate(forest):
        if index == 4:
            L = line.split('","')
            L[0] = L[0][1:]
            for i, item in enumerate(L):
                if item.isdigit():
                    if int(item) in years:
                        index_z.append(i)          
        elif index > 4:
            L = line.split('","')
            L[0] = L[0][1:]
            if L[index_z[1]] != '' and L[index_z[0]] != '':
                if float(L[index_z[1]]) > float(L[index_z[0]]):
                    dic[L[0]].append(float(L[index_z[1]])-float(L[index_z[0]]))





for key in dic:
    if len(dic[key]) == 2:
        result.append([key,dic[key][0]/dic[key][1]])

result = sorted(result, key = lambda d:d[0])
result = sorted(result, key = lambda d:d[1], reverse = True)

for i in range(len(result)):
    result[i][1] = round(float(result[i][1]),2) 



result_1 = []
for i in range(len(result)):
    string = result[i][0]+f' ({result[i][1]:.2f})'
    result_1.append(string)



if len(result_1)>top_n:
    for i in range(top_n):
        countries.append(result_1[i])
else:
    top_n = len(result_1)
    for i in range(len(result_1)):
        countries.append(result_1[i])


   








print(f'Here are the top {top_n} countries or categories where, between {year_1} and {year_2},\n'
      '  agricultural land and forest land areas have both strictly increased,\n'
      '  listed from the countries where the ratio of agricultural land area increase\n'
      '  to forest area increase is largest, to those where that ratio is smallest:')
print('\n'.join(country for country in countries))
    

