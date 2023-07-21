import random
number = random.randint(1,10)

number_of_guesses = 0

def check(number,number_of_guesses):
    guess = int(input('Plese enter a number in range => 1,10: '))
    number_of_guesses += 1
    if guess < number:
        return 'You shoud UP' , number_of_guesses
    elif guess > number:
        return 'You shoud DOWN', number_of_guesses
    if guess == number:
        return('You guessed the number in',str(number_of_guesses),'tries!')
    else:
        return('You did not guess the number, the number was',str(number))

while True:
    a = check(number,number_of_guesses)
    number_of_guesses = a[1]
    if "You guessed the number in" in a:
        print(" ".join(a))
        break
    print(a[0])