def gcd(x, y):
   if x > y:
       gcd_ = x
   else:
       gcd_ = y

   while(True):
       if((x % gcd_ == 0) and (y % gcd_ == 0)):
           break
       gcd_ -= 1

   return gcd_


number_1 = int(input("Plaese enter your number 1: "))
number_2 = int(input("Please enter your number 2:  "))
print("gcd: ",gcd(number_1, number_2))