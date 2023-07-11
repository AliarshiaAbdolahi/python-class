STR = input('Please enter your string: ')

A = reversed(STR)

B = "".join(A)

if B == STR:
    print('Yes,these are palindrome ✔')

else:
    print('NO,these are not palindrome ❌')