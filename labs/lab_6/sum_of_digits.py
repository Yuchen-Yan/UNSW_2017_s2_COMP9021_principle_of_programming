    
def solutions(available, sums):
    if sums < 0:
        return 0
    if available == 0:
        if sums == 0:
            return 1
        return 0

    return solutions(available//10, sums) + solutions(available//10, sums - available%10)






try:
    available = int(input('Input a number that we will use as available digits: '))
    sums = int(input('Input a number that represents the desired sum: '))
except ValueError:
    print('invalid input, giving up...')
    sys.exit()


result = solutions(available, sums)


if result == 0:
    print('There is no solution.')
elif result == 1:
    print('There is a unique solution.')
else:
    print(f'There are {result} solutions.')
