def sum(number):
    return f"{number}{number+number}{number+number+number}"

number = int(input("Please enter your number: "))
print("Your answer is:",sum(number))