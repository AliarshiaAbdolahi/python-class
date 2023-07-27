import random

cars = ["Nissan Skylan R34","BMW X4","Alfa Romeo","Aston Martin","Toyota Supra","Benz Maybach","Benz G Class","Bentley","rolls Royce","Lamborghini Aventador","Dodge Challenger","Benz T80","Pride 132","Chery","Chevrolet Camaro","Ford Mustang"]
colors = ["red","orange","yellow","green","blue","purple","silver","gold","brown","gray","black","white"]
max_speed = [180,185,190,623,200,205,210,215,220,500,230,235,240,245,250]
Car_specifications = {}

for i in range(len(cars)):
    Car_specifications.update({f"name{i}" : f"{cars[i]}"})
    color = random.choice(colors)
    Car_specifications.update({f"color {cars[i]}" : f"{color}"})
    speed = random.choice(max_speed)
    Car_specifications.update({f"speed {cars[i]}" : f"{speed}"})

while True:
    print("""
1_(Find)
2_(Clear)
3_(Show all)
4_(Del item)
5_(Keys)
6_(Values)
7_(Exit)
""")
    
    User = (input("Please enter your choice: "))

    if User == '1':
        A = input("key: ")
        print(Car_specifications.get(A))

    elif User == '2':
        Car_specifications.clear()
        print("clear successfully!!")
    
    elif User == '3':
        print("items")
        print(Car_specifications.items())
    
    elif User == '4':
        A = input("key: ")
        Car_specifications.pop(A)
        print("delet successfully!!")

    elif User == '5':
        print("keys")
        print(Car_specifications.keys(), end=",")
    
    elif User == '6':
        print("values")
        print(Car_specifications.values(), end=",")

    elif User == '7':
        break
