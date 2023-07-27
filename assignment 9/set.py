import random

numbers = {0}
A = 0
B = 0

while True:
    C = random.randint(1,50)
    for i in range(C):
        D = random.randint(1,100)
        numbers.add(D)
    print(numbers)

    numbers_2 = numbers.copy()
    for i in range(len(numbers_2)):
        if list(numbers_2)[i] % 2 != 0:
            A += 1
        else:
            B += 1
    if A > B:
        numbers_2.clear()
    else:
        for i in range(len(numbers_2)):
            if i >= len(numbers_2):
                break
            if list(numbers_2)[i] % 2 != 0:
                numbers_2.remove(list(numbers_2)[i])
        numbers.update(numbers_2)
        break
    print(numbers)