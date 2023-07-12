import random
number = random.randint(1,10)

number_of_guesses = 0

while number_of_guesses < 5:
    guess = int(input('Plese enter a number in range => 1,10: '))
    number_of_guesses += 1
    if guess < number:
        print('You shoud UP')
    elif guess > number:
        print('You shoud DOWN')
    elif guess == number:
        break
if guess == number:
    print('You guessed the number in',str(number_of_guesses),'tries!')
else:
    print('You did not guess the number, the number was',str(number))