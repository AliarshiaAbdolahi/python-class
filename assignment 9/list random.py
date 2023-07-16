import random

numbers = []

while True:
    print("Please your number < 100")
    operation = int(input("Please enter your number: "))
    break
while len(numbers) < operation:
    number = random.randint(1,100)
    if number in numbers:
        continue
    else:
        numbers.append(number)
print(numbers)