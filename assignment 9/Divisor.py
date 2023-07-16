number = int(input("please enter your number: "))
answer = 0
for i in range(1,number):
    if number % i == 0:
        answer += i
if answer == number:
    print("Yes,this number is correct")
else:
    print("No,this number is wrong")