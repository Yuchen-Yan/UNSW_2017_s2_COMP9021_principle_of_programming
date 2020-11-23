# Written by Yuchen Yan for comp9021 lab 1 question1


'''
Prints out a conversion table of temperatures from Celsius to Fahrenheit degrees,
with the former ranging from 0 to 100 in steps of 10.
'''


min_temperature = 0
max_temperature = 100
step = 10
print('Celsius\tFahrenheit')

for celsius in range(min_temperature, max_temperature + step, step):
    fahrenheit = celsius * 9 / 5 +32
    print(f'{celsius:7d}\t{int(fahrenheit):10d}')
