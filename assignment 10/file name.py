file_name = input("Please enter your file name: ")
file_name = file_name.split(" ")

for name in file_name:
    A = 0
    B = 0
    if "." in name:
        C = name.split(".")
        for i in ("0","1","2","3","4","5","6","7","8","9"):
            if i in C[1]:
                print(f"There is a number in the {name} suffix")
                A += 1
                break
            
        if len(C[1]) == 1 or len(C[1]) > 3:
            print(f"The problem is in the number of letters in the suffix of the {name}")
            A += 1
        
        elif C[1] == "err":
                print(f"The {name} suffix is equal to 'err'")
                A += 1

    else:
        print(f"in {name} '.' not find")
        A += 1
    
    for i in ("0","1","2","3","4","5","6","7","8","9"):
        B += name.count(i)
        if B > 3:
            print(f"There are more than 3 numbers in the {name}")
            A += 1
            break

    for i in ("0","1","2","3","4","5","6","7","8","9"): 
        if name[0] == i:
            print(f"name {name} starts with a number")
            A += 1
    
    if A == 0:
        print(f"{name} is acceptable")
    else:
        print(f"{name} is not acceptable")