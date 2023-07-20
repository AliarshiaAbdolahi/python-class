def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b 

operation = int(input("How many sequences of Fibonacci numbers do you want? "))
print(f"Its sequence of {operation} becomes:",fibonacci(operation))