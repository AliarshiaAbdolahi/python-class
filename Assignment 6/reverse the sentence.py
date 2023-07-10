TXT = input('Please enter your sentence:')

TXT = TXT[::-1]

TXT = TXT.split()

TXT ="*".join(TXT)

print(TXT)