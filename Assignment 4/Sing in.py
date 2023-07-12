Username_1 = 'aliarshia' 
Password_1 = '1388' 

Username = input('Please enter your Username:') 
Password = input('Please enter your Password:') 
 
if Username == Username_1 and Password == Password_1: 
    print('It is ture') 
 
elif Username == Username_1 or Password == Password_1:
    Username = input('Please enter your Username:') 
    Password = input('Please enter your Password:') 
    if Username == Username_1 and Password == Password_1: 
        print('It is ture')
    else:
        print("is not true")
else:
    print("is not true")