def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x % y)
    
x = int(input("Please enter number 1: "))
y = int(input("Please enter number 2: "))
print("Answer is:",GCD(x,y))