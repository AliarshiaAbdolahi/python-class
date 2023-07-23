X = int(input("Please enter your (X): "))
Y = int(input("Please enter your (Y): "))

for i in range(1,Y+1):
    for j in range(1,X+1):
        print(j * i,end="   ")
    print()
