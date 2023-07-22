n = int(input("Enter the diameter of the rhombus: "))

for i in range(1,n+1):
    print((n-i)*' '+(2*i-1)*'*')

for i in range(1,n+1):
    print((i)*' '+(-2*i + (2*n-1))*'*')