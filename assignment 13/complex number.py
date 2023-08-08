def sum(dictionary):
    return f"{dictionary['A'] + dictionary['A2']} , {dictionary['B'] + dictionary['B2']}"

def sub(dictionary):
    return f"{dictionary['A'] - dictionary['A2']} , {dictionary['B'] - dictionary['B2']}"

operation =input('''
1_(sum)
2_(subtraction)
Please enter your choice: ''')
print()

A = float(input("Please enter number (a): "))
B = float(input("Please enter number (b): "))

print()
print("number 2:\n")

A_2 = float(input("Please enter number (a): "))
B_2 = float(input("Please enetr number (b): "))

dictionary = {"A": A, "B": B, "A2": A_2, "B2": B_2} 

if operation == "1":
    print(sum(dictionary))
elif operation == "2":
    print(sub(dictionary))