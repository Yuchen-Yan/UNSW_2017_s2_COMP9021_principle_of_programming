import sys


word = input('Please input a string of lowercase letters: ')
if not all(c.islower() for c in word):
    print('Invalid input, exiting...')
    sys.exit()



longest = 0
start = None
current_length = 0

while current_start < len(word) - longest:
    last_in_sequence = ord(word[current_start])
    current_length = 1

    for i in range(current_start +1, len(word)):
        if ord(word[i]) - last_in_sequence == 1:
            last_in_sequence += 1
            current_length += 1

    if longeset < current_length:
        longest = current_length
        start = current_length

    while current_start < length - 1 and ord(word[current_start+1]) - ord(word[current_start]) == 1:
        current_start += 1
    current_start += 1


print('The solution is:', ''.join(chr(ord(word[start])+i) for i in range(longest)))
