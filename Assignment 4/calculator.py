import math

operation = input('''
Please type in the math operation you would like to complete:
1_(+) for addition
2_(-) for subtraction
3_(*) for multiplication
4_(/) for division
5_(**) for power
6_(sin)
7_(cos)
8_(tan)
9_(round)
10_(factorial)
11_(sqrt)
''')

if operation == '1' or operation == '2' or operation == '3' or operation == '4' or operation == '5': 

        number_1 = float(input('Please enter the first number: '))
        number_2 = float(input('Please enter the second number: '))

elif operation == '6' or operation == '7' or operation == '8' or operation == '9' or operation == '10' or operation == '11':

        number_1 = float(input('Please enter the first number: '))

if operation == '1':
        result = number_1 + number_2
        print(f"{number_1} + {number_2} = {result}")

elif operation == '2':
        result = number_1 - number_2
        print(f"{number_1} - {number_2} = {result}")

elif operation == '3':
        result = number_1 * number_2
        print(f"{number_1} * {number_2} = {result}")

elif operation == '4':
         result = number_1 / number_2
         print(f"{number_1} / {number_2} = {result}")

elif operation == '5':
        result = number_1 ** number_2
        print(f"{number_1} ** {number_2} = {result}")

elif operation == '6':
     n=math.radians(number_1)
     result = math.sin(n)

elif operation == '7':
        n = math.radians(number_1)
        result = math.cos(n)

elif operation == '8':
        n = math.radians(number_1)
        result = math.tan(n)

elif operation == '9':
        result = round(number_1)

elif operation == '10':
        result = math.factorial(number_1)

elif operation == '11':
        result = math.sqrt(number_1)              

else:
        print('You have not typed a valid operator, please run the program again.')

print(result)