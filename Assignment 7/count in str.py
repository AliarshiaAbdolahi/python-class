STR = input('Please enter a string: ')

A = input('Please enter a word: ')
B = 0

for i in range(len(STR)):
    if STR[i] == A:
        B += 1

print(B)