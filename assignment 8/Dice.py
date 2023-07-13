import random

A = 1
B = 6
number = 0
total = 0

while number != 6:
    number = random.randint(A,B)
    print(number)
    total += number

print('sum = ',total)