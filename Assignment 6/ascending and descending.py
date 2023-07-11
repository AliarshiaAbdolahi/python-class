numbers = input('Please enter your numbers(please enter with spaces:1 2 3 4 5 6 7 8 9): ')

answer = numbers.split()

A = sorted(answer)
print(A)

B = sorted(answer, reverse=True)
print(B)