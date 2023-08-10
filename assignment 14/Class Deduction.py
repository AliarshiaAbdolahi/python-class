def show(a,b):
    print("  "+str(a)+ "\n-----\n  "+ str(b))

class Deduction:
    def __init__(self, dictionary1 , dictionary2):
        self.dictionary_1, self.dictionary_2 = dictionary1, dictionary2
    
    def Multiplication(self):
        The_numerator, Denominator = self.dictionary_1["The_numerator"] * self.dictionary_2["The_numerator"], self.dictionary_1["Denominator"] * self.dictionary_2["Denominator"]
        return The_numerator , Denominator

    def Subtraction(self):
        The_numerator, Denominator = (self.dictionary_1["The_numerator"] * self.dictionary_2["Denominator"]) - (self.dictionary_2["The_numerator"] * self.dictionary_1["Denominator"]), self.dictionary_1["Denominator"] * self.dictionary_2["Denominator"]
        return The_numerator, Denominator
    
    def Sum(self):
        The_numerator, Denominator = (self.dictionary_1["The_numerator"] * self.dictionary_2["Denominator"]) + (self.dictionary_2["The_numerator"] * self.dictionary_1["Denominator"]), self.dictionary_1["Denominator"] * self.dictionary_2["Denominator"]
        return The_numerator, Denominator

    def Division(self):
        The_numerator, Denominator = self.dictionary_1["The_numerator"] * self.dictionary_2["Denominator"], self.dictionary_1["Denominator"] * self.dictionary_2["The_numerator"]
        return The_numerator, Denominator
    
operation = int(input("1=Sum\n2=Subtraction\n3=Multiplication\n4=Division\nPlease enter your choice: "))

for i in range (2):
    The_numerator = float(input("Please enter the numerator: "))
    Denominator = float(input("Please enter denumerator: "))

    if i == 0:
        dct1  = {"The_numerator": The_numerator, "Denominator": Denominator}
    else:
        dct2 = {"The_numerator": The_numerator, "Denominator": Denominator}

deduction = Deduction(dct1, dct2)

if operation == 1:
    s,m = deduction.Sum()
    show(s,m)
elif operation == 2:
    s,m = deduction.Subtraction()
    show(s,m)
elif operation == 3:
    s,m = deduction.Multiplication()
    show(s,m)
elif operation == 4:
    s,m = deduction.Division()
    show(s,m)