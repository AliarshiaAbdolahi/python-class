import ast


number = int(input('Please enter your number:'))

X = number % 2

if number == 0:
    print('The number 0 is not defined')

elif number < 0:
    print('These number are not defined')

elif X == 0:
    print('This',number,'is EVEN' )

elif X == 1:
    print('This',number,'is ODD')

number = str(number)

A = number.count("1")
B = number.count("3")
C = number.count("5")
D = number.count("7")
E = number.count("9")
F = number.count("0")
G = number.count("2")
H = number.count("4")
I = number.count("6")
J = number.count("8")

ODD =A + B + C + D 

EVEN =F + G + H + I +J

if ODD < EVEN:
    print('EVEN')

elif EVEN > ODD:
    print(ODD)