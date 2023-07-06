operation = input('''
1_centigrade to kelvin
2_centigrade to farahite
3_kelvin to centigrade
4_kelvin to farahite
5_farahite to centigrade
6_farahite to kelvin
''')

number = float(input('Please enter the weather: '))

if operation == '1':
    print('centigrade to kelvin is:',number + 273.15)

elif operation == '2':
    print('centigrade to farahite is:',(1.8 * number) + 32)

elif operation == '3':
    print('kelvin to centigrade is:',number - 273.15)

elif operation == '4':
    print('kelvin to farahite is:',(number * 1.8) - 459.67)

elif operation == '5':
    print('farahite to centigrade',(number - 32) / 1.8)

elif operation == '6':
    print('farahite to kelvin',(number + 459.67) / 1.8)

else:
    print('Try agin')