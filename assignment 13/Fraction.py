def sum(Fraction_1,Fraction_2):
    The_numerator = (Fraction_1["The_numerator"] * Fraction_2["Denominator"]) + (Fraction_2["The_numerator"] * Fraction_1["Denominator"])
    Denominator = Fraction_1["Denominator"] * Fraction_2["Denominator"]
    return The_numerator,Denominator

def subtraction(Fraction_1,Fraction_2):
    The_numerator = (Fraction_1["The_numerator"] * Fraction_2["Denominator"]) - (Fraction_2["The_numerator"] * Fraction_1["Denominator"])
    Denominator = Fraction_1["Denominator"] * Fraction_2["Denominator"]
    return The_numerator,Denominator

def multiplication(Fraction_1,Fraction_2):
    The_numerator = Fraction_1["The_numerator"] * Fraction_2["The_numerator"]
    Denominator = Fraction_1["Denominator"] * Fraction_2["Denominator"]
    return The_numerator,Denominator

def Division(Fraction_1,Fraction_2):
    if Fraction_2['Denominator'] != 0 and Fraction_2["The_numerator"] != 0:
        The_numerator = Fraction_1["The_numerator"] * Fraction_2["Denominator"]
        Denominator = Fraction_1["Denominator"] * Fraction_2["The_numerator"]
        return The_numerator,Denominator
    else:
        return "The number you entered for (The_numerator) or (Denominator) is equal to 0"
    
operation = input('''
1_(sum)
2_(subtraction)
3_(multiplication)
4_(Division)\n
Please enter your choice: ''')
print()

The_numerator_1 = int(input("Please enter the The_numerator: "))
Denominator_1 = int(input("Please enter the Denominator: "))
dictionary_1 = {"The_numerator":The_numerator_1,"Denominator":Denominator_1}

print()
print("Fraction 2\n")

The_numerator_2 = int(input("Please enter the The_numerator_2: "))
Denominator_2 = int(input("Please enter the Denominator_2: "))
dictionary_2 = {"The_numerator":The_numerator_2,"Denominator":Denominator_2}

if operation == "1":
    A,B =  sum(dictionary_1,dictionary_2)
    print(A,"\n-----\n",B)

elif operation == "2":
    A,B =  subtraction(dictionary_1,dictionary_2)
    print(A,"\n-----\n",B)

elif operation == "3":
    A,B =  multiplication(dictionary_1,dictionary_2)
    print(A,"\n-----\n",B)

elif operation == "4":
    A,B =  Division(dictionary_1,dictionary_2)
    print(A,"\n-----\n",B)

