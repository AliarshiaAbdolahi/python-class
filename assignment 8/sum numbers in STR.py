str = input('Please enter your string: ')
numbers = ['1','2','3','4','5','6','7','8','9']
count = 0

for i in range(len(str)):
    for j in range(len(numbers)):
        if str[i] == numbers[j]:
            count += int(numbers[j])

print(count)