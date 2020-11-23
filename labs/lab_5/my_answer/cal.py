#This is written by Yuchen Yan


'''
My calendar generator, tart the first day of week by monday
'''

import calendar


print('I will display a calendar, either for a year or for a month in a year.')
print('The earliest year should be 1753.')
print('For the month, input at least the first three letters of the month’s name.')
while True:
    try:
        input_value = input('Input year, or year and month, or month and year:')
        value = input_value.split()
        for i in range(len(value)):
            if len(value)==1:
                month = False
            if value[i].isdigit():
                year = value[i]
            else:
                month = value[i]
        if int(year) < 1753:
            raise ValueError
        else:
            break
    except ValueError:
        print('Invlid input, try again...')    

year = int(year)

if month:
    month = list(month)
    for i in range(len(month)):
        month[i] = month[i].lower()
    if 'j' in month and 'a' in month and 'n' in month:
        month = 'January'
        monthn = 1
    elif 'f' in month and 'e' in month and 'b' in month:
        month = 'February'
        monthn = 2
    elif 'm' in month and 'a' in month and 'r' in month:
        month = 'March'
        monthn = 3
    elif 'a' in month and 'p' in month and 'r' in month:
        month = 'April'
        monthn = 4
    elif 'm' in month and 'a' in month and 'y' in month:
        month = 'May'
        monthn = 5
    elif 'j' in month and 'u' in month and 'n' in month:
        month = 'June'
        monthn = 6
    elif 'j' in month and 'u' in month and 'l' in month:
        month = 'July'
        monthn = 7
    elif 'a' in month and 'u' in month and 'g' in month:
        month = 'August'
        monthn = 8
    elif 's' in month and 'e' in month and 'p' in month:
        month = 'September'
        monthn = 9
    elif 'o' in month and 'c' in month and 't' in month:
        month = 'October'
        monthn = 10
    elif 'n' in month and 'o' in month and 'v' in month:
        month = 'November'
        monthn = 11
    elif 'd' in month and 'e' in month and 'c' in month:
        month = 'December'
        monthn = 12
      



if month:
    cal = calendar.month(1700,monthn)
    print(cal)
else:
    cal = calendar.calendar(year)
    print(cal)






