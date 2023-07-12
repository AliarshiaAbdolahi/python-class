Decimal_number = float(input('Please enter one decimal number:'))
Ikan = int(input('Please enter ikan:'))
Dahgan = int(input('Please enter dahgan:'))
Sadgan = int(input('Please enter sadgan:'))
Hezargan = int(input('Please enter hezargan:'))

A = Decimal_number / 10
B = Dahgan * 10
C = Sadgan * 100
D = Hezargan * 1000

answer = A + B + C + D
print(answer)