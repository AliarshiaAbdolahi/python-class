import random

print('''Hello...
welcome to the number guessing game
      
here you have to help me to guess your number:
1_(T)=>it is [True]
2_(U)=>go [up]
3_(D)=>go [down]
''')
A = 1
B = 99
C = 0

guess = random.randint(A,B)
print('It your number is:',guess)

operation = input('Please direct me: ')
while operation != 'T':
    C += 1
    if operation == 'D':
        B = guess
        guess = random.randint(A,B)
        print('It your number is:',guess)
        operation = input('Please direct me: ')
    elif operation == 'U':
        A = guess
        guess = random.randint(A,B)
        print('It your number is:',guess)
        operation = input('Please direct me: ')

print('Well done, you were able to guess my number')
print('You guessed the number in',str(C),'tries!')