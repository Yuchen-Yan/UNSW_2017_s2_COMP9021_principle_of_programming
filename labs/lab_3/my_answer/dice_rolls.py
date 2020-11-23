#This is writen by Yuchen Yan for lab3 question 5

'''
This is about dice rolling
'''

from random import randint
from pygal import Bar
from pygal.style import Style


sides = input('Enter N strictly positive integers (number of sides of N dice): ')
L = list(sides.split())
flag = False

if len(L) == 0:
    print('You did not enter any value, a single standard six-sided die will be rolled.')
    L.append(6)
else:
    for i in range(len(L)):
        if L[i].isdigit():
            if int(L[i]) <= 0:
                L[i] = 6
                flag = True
            else:
                L[i] = int(L[i]) 
            pass
        else:
            L[i] = 6
            
            flag = True

        
if flag:
    print('Some of the values, incorrect, have been replaced with the default value of 6.')

print()


roll = input('Enter the desired number of rolls: ')

if roll.isdigit() and int(roll) > 0:
    roll = int(roll)
else:
    roll = 2000
    print('Input was not provided or invalid, so the default value of 1,000 will be used.')




L = sorted(L)

result = []
for i in range(roll):
    sums = 0
    for j in range(len(L)):
        sums += randint(1,L[j])
    result.append(sums)
    
range_of_sums = list(set(result))    
counts = [result.count(i) for i in range_of_sums]
counts = [{'value':count, 'label': f'Frequency: {count / roll:.2f}'} for count in counts]




histogram = Bar(style = Style(colors = ('#228B22',), major_label_font_size = 12), show_legend = False)
histogram.title = f'Simulation for {roll} rolls of the dice: {sorted(L)}'
histogram.x_labels = [str(i) for i in range_of_sums]
histogram.x_title = 'Possible sums'
histogram.y_title = 'Counts'
histogram.add('', counts)
histogram.render_to_file('dice_rolls.svg')





























