password_save = 1234
ask_password = 4321

for i in range(3):
    password = int(input("Please enter your password: "))

    if password == password_save:
        print('welcome')
        break
    elif password == ask_password:
        print('The police were informed...!')
        break
    elif i == 2:
        print(" Your account has been blocked...!")