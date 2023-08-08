operation = input('''
1_(sum)
2_(subtraction)
Please enter your choice: ''')
print()

Hour_1 = int(input("Please enter the hour: "))
Minutes_1 = int(input("Please enter the Minutes: "))
Second_1 = int(input("Please enter the Second: "))
Time_1 = {"hour":Hour_1,"minutes":Minutes_1,"second":Second_1}

print()
print("Time 2\n")

Hour_2 = int(input("Please enter the hour: "))
Minutes_2 = int(input("Please enter the Minutes: "))
Second_2 = int(input("Please enter the Second: "))
Time_2 = {"hour":Hour_2,"minutes":Minutes_2,"second":Second_2}

if operation == "1":
    H = Time_1["hour"] + Time_2["hour"]
    M = Time_1["minutes"] + Time_2["minutes"]
    S = Time_1["second"] + Time_2["second"]
    while not(0 <= S <= 60 and 0 <= M <= 60):
        if S >= 60:
            S -= 60
            M += 1
        if S < 0:
            M -= 1
            S += 60
        if M >= 60:
            M -= 60
            H += 1
        if M < 0:
            H -= 1
            M += 60
    print(f"{H}:{M}:{S}")

elif operation == "2":
    H = Time_1["hour"] - Time_2["hour"]
    M = Time_1["minutes"] - Time_2["minutes"]
    S = Time_1["second"] - Time_2["second"]
    while not(0 <= S <= 60 and 0 <= M <= 60):
        if S < 0:
            M -= 1
            S += 60
            if M < 0:
                H -= 1
                M += 60
    print(f"{H}:{M}:{S}")
