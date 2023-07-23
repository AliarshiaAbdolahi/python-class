def check(Sentence):
    capital = 0
    small = 0
    for i in Sentence:
        if 65 <= ord(i) <= 90:
            capital += 1
        if 97 <= ord(i) <= 122:
            small += 1
            return capital,small
        
Sentence = input("Please enter your Sentence:\n")
capital,small = check(Sentence)
print("capital:",capital)
print("small:",small)