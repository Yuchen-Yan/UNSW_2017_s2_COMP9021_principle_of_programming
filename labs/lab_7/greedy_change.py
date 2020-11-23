
face = [1, 2, 5, 10, 20, 50, 100]
amount = int(input('Input the desired amount: '))
amount_left = amount
banknote = []

while amount_left:
    money = face.pop()
    if amount_left >= money:
        banknote.append((money,amount_left//money))
        amount_left %= money

nb_of_note = sum(note[1] for note in banknote)
print()
if nb_of_note == 1:
    print('1 banknote is needed')
else:
    print(f'{nb_of_note} banknote are needed')


print('The detail is:')
for note in banknote:
    print(f'{"$"+str(note[0]):>4}: {note[1]}')
