number = float(input('Please enter your number: '))

A = number % 2

if number < 0:
    print('D')

elif A == 0 and number >= 6:
    print('A')

elif A == 0 and number <= 4:
    print('B')

else:
    print('C')