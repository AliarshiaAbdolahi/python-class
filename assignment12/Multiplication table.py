R = int(input("Please enter your (row): "))
C = int(input("Please enter your (col): "))

for i in range(1,C+1):
    for j in range(1,R+1):
        print(j * i,end="   ")
    print()