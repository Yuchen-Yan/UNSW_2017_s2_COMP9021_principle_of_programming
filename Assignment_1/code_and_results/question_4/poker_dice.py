#written by Yuchen Yan Vincent for comp9021 assignment1 question 4

'''
Write a program named poker_dice.py that simulates the roll of 5 dice,
at most three times, as described at http://en.wikipedia.org/wiki/Poker_dice
as well as a given number of rolls of the 5 dice to evaluate the
probabilities of the various hands.
'''


from random import randint










def play():
#first roll
    L = [randint(0,5),randint(0,5),randint(0,5),randint(0,5),randint(0,5)]
    L = sorted(L)
        
    dic = {0:'Ace', 1:'King', 2:'Queen', 3:'Jack', 4:'10', 5:'9'}
    dic_r = {'Ace':0, 'King':1, 'Queen':2, 'Jack':3, '10':4, '9':5}
    
    print('The roll is:', dic[L[0]], dic[L[1]], dic[L[2]], dic[L[3]], dic[L[4]],)
    C = [L.count(L[0]), L.count(L[1]), L.count(L[2]), L.count(L[3]), L.count(L[4])]

    if 5 in C:
        print('It is a Five of a kind')
    elif 4 in C:
        print('It is a Four of a kind')
    elif 3 in C and 2 in C:
        print('It is a Full house')
    elif (C.count(1)==5 and 5 not in L) or (C.count(1)==5 and 0 not in L):
        print('It is a Straight')
    elif 3 in C and 1 in C:
        print('It is a Three of a kind')
    elif C.count(2)==4:
        print('It is a Two pair')
    elif C.count(2)==2 and C.count(1)==3:
        print('It is a One pair')
    else:
        print('It is a Bust')









        
#Asking for keep first time
    while True:
        keep = input('Which dice do you want to keep for the second roll? ')
        if keep == 'All' or keep == 'all':
            print('Ok, done.')
            return
        keep = keep.split()
        if len(keep) == 0:
#            print('work')
            break
        try:
            for index in range(len(keep)):
                if keep[index] in dic_r.keys() and keep[index] in [dic[L[e]] for e in range(len(L))]:
                    keep[index] = dic_r[keep[index]]
                else:
                    raise ValueError
        except ValueError:
            print('That is not possible, try again!')
            continue
        break
    if sorted(keep) == sorted(L):
        print('Ok, done.')
        return
#Roll the second time with keep or not
    if len(keep) == 0:
        L = [randint(0,5),randint(0,5),randint(0,5),randint(0,5),randint(0,5)]
    else:
        new = []
        for i in range(5-len(keep)):
            new.append(randint(0,5))
        L = keep+new
    L = sorted(L)
    print('The roll is:', dic[L[0]], dic[L[1]], dic[L[2]], dic[L[3]], dic[L[4]],)
    C = [L.count(L[0]), L.count(L[1]), L.count(L[2]), L.count(L[3]), L.count(L[4])]
#Decide the result second time
    if 5 in C:
        print('It is a Five of a kind')
    elif 4 in C:
        print('It is a Four of a kind')
    elif 3 in C and 2 in C:
        print('It is a Full house')
    elif (C.count(1)==5 and 5 not in L) or (C.count(1)==5 and 0 not in L):
        print('It is a Straight')
    elif 3 in C and 1 in C:
        print('It is a Three of a kind')
    elif C.count(2)==4:
        print('It is a Two pair')
    elif C.count(2)==2 and C.count(1)==3:
        print('It is a One pair')
    else:
        print('It is a Bust')









        
#Asking for keep second time
    while True:
        keep = input('Which dice do you want to keep for the third roll? ')
        if keep == 'All' or keep == 'all':
            print('Ok, done.')
            return
        keep = keep.split()
        if len(keep) == 0:
#            print('work')
            break
        try:
            for index in range(len(keep)):
                if keep[index] in dic_r.keys() and keep[index] in [dic[L[e]] for e in range(len(L))]:
                    keep[index] = dic_r[keep[index]]
                else:
                    raise ValueError
        except ValueError:
            print('That is not possible, try again!')
            continue
        break
    if sorted(keep) == sorted(L):
        print('Ok, done.')
        return
#Roll the third time with keep or not
    if len(keep) == 0:
        L = [randint(0,5),randint(0,5),randint(0,5),randint(0,5),randint(0,5)]
    else:
        new = []
        for _ in range(5-len(keep)):
            new.append(randint(0,5))
        L = new+keep

    L = sorted(L)
    print('The roll is:', dic[L[0]], dic[L[1]], dic[L[2]], dic[L[3]], dic[L[4]],)
    C = [L.count(L[0]), L.count(L[1]), L.count(L[2]), L.count(L[3]), L.count(L[4])]
#Decide the result second time
    if 5 in C:                   
        print('It is a Five of a kind')
    elif 4 in C:
        print('It is a Four of a kind')
    elif 3 in C and 2 in C:
        print('It is a Full house')
    elif (C.count(1)==5 and 5 not in L) or (C.count(1)==5 and 0 not in L):
        print('It is a Straight')
    elif 3 in C and 1 in C:
        print('It is a Three of a kind')
    elif C.count(2)==4:
        print('It is a Two pair')
    elif C.count(2)==2 and C.count(1)==3:
        print('It is a One pair')
    else:
        print('It is a Bust')



















        
def simulate(n):
    p = [0,0,0,0,0,0,0]
    five = 0
    four = 0
    full = 0
    straight = 0
    three = 0
    two = 0
    one = 0
    for i in range(n):
        L = [randint(0,5),randint(0,5),randint(0,5),randint(0,5),randint(0,5)]
        C = [L.count(L[0]), L.count(L[1]), L.count(L[2]), L.count(L[3]), L.count(L[4])]

        if 5 in C:
            five += 1
            
        elif 4 in C:
            four += 1
            
        elif 3 in C and 2 in C:
            full += 1
            
        elif (C.count(1)==5 and 5 not in L) or (C.count(1)==5 and 0 not in L):
            straight += 1
            
        elif 3 in C and 1 in C:
            three += 1
            
        elif C.count(2)==4:
            two += 1
            
        elif C.count(2)==2 and C.count(1)==3:
            one += 1
            
        else:
            continue

    p[0] = five/n * 100
    p[1] = four/n * 100
    p[2] = full/n * 100
    p[3] = straight/n * 100
    p[4] = three/n * 100
    p[5] = two/n * 100
    p[6] = one/n * 100

    print(f'Five of a kind : {p[0]:.2f}%')
    print(f'Four of a kind : {p[1]:.2f}%')
    print(f'Full house     : {p[2]:.2f}%')
    print(f'Straight       : {p[3]:.2f}%')
    print(f'Three of a kind: {p[4]:.2f}%')
    print(f'Two pair       : {p[5]:.2f}%')
    print(f'One pair       : {p[6]:.2f}%') 




    




