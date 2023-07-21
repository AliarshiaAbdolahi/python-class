import math

a = float(input("Please enter your number (a): "))
b = float(input("Please enter your number (b): "))
c = float(input("Please enter your number (c): "))

def Eq(a,b,c):
    if a != 0:
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / 2 * a
            x2 = (-b - math.sqrt(delta)) / 2 * a
            return(f' The equation has two real roots : \n x1 = {x1} \n x2 = {x2} ')
        elif delta == 0:
            x_conj = -b / 2 * a
            return(f' The equation has one conj root : {x_conj}')
        elif delta < 0:
            return(' The equation has not root(s) ')
    elif a == 0:
        return(" Coefficient error : 'a' can not be zero, the following equation is linear")

print(Eq(a,b,c))