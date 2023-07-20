def lcm(x, y):
   if x > y:
       lcm_ = x
   else:
       lcm_ = y

   while(True):
       if((lcm_ % x == 0) and (lcm_ % y == 0)):
           break
       lcm_ += 1

   return lcm_


number_1 = int(input("Plaese enter your number 1: "))
number_2 = int(input("Please enter your number 2:  "))
print("lcm: ",lcm(number_1, number_2))