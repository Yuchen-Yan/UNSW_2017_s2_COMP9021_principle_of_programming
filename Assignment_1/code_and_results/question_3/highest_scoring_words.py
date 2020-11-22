# This is written by Yuchen Yan


'''
This program is aim to find the highest score in the words build by
the characters, which are input by users.
'''
#from itertools import permutations 


#get the lowercase letters which are between 3 and 10 
def input_char():
    L = []
    try:
        input_value = input('Enter between 3 and 10 lowercase letters: ')
        list(input_value)
        for e in input_value:
            if e !=' ':
                if e.islower():
                    L.append(e)
                elif e.isdigit():
                    raise ValueError
                elif e.isupper():
                    raise ValueError
                else:
                    raise ValueError
                
        if len(L) < 3 or len(L) > 10:
            raise ValueError
            
    except ValueError:
        print('Incorrect input, giving up...')
        exit()
    return L






#In the main function

if __name__ == '__main__':
#initail some viariables
    L = []
    L = input_char()
    word = set()
    
    highest_score = 0
    highest_item = set()
    h_i = ''
    word_score = {'a':2, 'b':5, 'c':4, 'd':4, 'e':1, 'f':6, 'g':5, 'h':5, 'i':1, 'j':7, 'k':6, 'l':3, 'm':5, 'n':2, 'o':3, 'p':5, 'q':7, 'r':2, 's':1, 't':2, 'u':4, 'v':6, 'w':6, 'x':7, 'y':5, 'z':7}


#Read in all the words in the file
    file = open('wordsEn.txt')
 
    for line in file:
        flag = False
        w = line.strip('\n')
        line = list(w)
        #print(w)
        answer = []
        for e in range(len(L)):
            answer.append(L[e])
            
        #print(answer)
        for i in range(len(line)):
            if line[i] in answer:
                answer.remove(line[i])
            else:
                flag = True
                break
        #print(w)
        if flag:
            continue
        word.add(w)
            
    file.close()



#Decide whether no word is built or not
    if len(word) == 0:
        print('No word is built from some of those letters.')
        
#find the highest scoring items
    else:
        for item_2 in word:
            each_word = list(item_2)
            score = 0
            for item_3 in each_word:
                score += word_score[item_3]
            if highest_score < score:
                highest_score = score
                h_i = item_2
        highest_item.add(h_i)
        
        for item_4 in word:
            each_word = list(item_4)
            score = 0
            for item_5 in each_word:
                score += word_score[item_5]
            if highest_score == score and item_4 not in highest_item:
                highest_item.add(item_4)

#print the items and the score
        highest_item = list(highest_item)
        print(f'The highest score is {highest_score}.')
        if len(highest_item) == 1:
            print('The highest scoring word is',highest_item[0]) 
        else:
            highest_item.sort()
            print('The highest scoring words are, in alphabetical order:')
            for item_6 in highest_item:
                print('   ',item_6)























        




