number = int(input('Please enter your number: '))

X = number % 7

if number == 0:
    print('Please try agin')

elif X == 0:
    print('True')

number = number // 7
number *= 7
number += 7

print(number)