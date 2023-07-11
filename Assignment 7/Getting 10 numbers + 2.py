list_1 = []
A = 0
for i in range (10):
    A = float(input('Please enter your number: '))
    list_1.append(A)

list_2 = []
B = 0
while B < 10:
    list_2.append(list_1[B] + 2)
    B += 1

print(list_1)
print(list_2)