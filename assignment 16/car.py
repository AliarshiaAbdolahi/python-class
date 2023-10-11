import json
import csv

car = []
with open("D:/python course/assignment 16/cars_dataset.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        car.append(row)

def show(car):
    for i in range(len(car)):
        print("="*100)
        print(car[i])
    
def japan_cars(car):
    japancars = []
    for i in range(len(car)):
        if car[i][8] == "Japan":
            japancars.append(car[i])
    print(show(japancars))
    return japancars

def longe_name(car):
    c = 0
    for i in range(len(car)):
        if len(car[i][0]) > c:
            heighestname = tuple(car[i])
            c = len(car[i][0])
    print(show(heighestname))
    return heighestname

def small_name(car):
    c = 10
    for i in range(len(car)):
        if len(car[i][0]) < c:
            shortestname = tuple(car[i])
            c = len(car[i][0])
    print(show(shortestname))
    return shortestname

def Cylinders_average(car):
    c = 0
    for i in range(len(car)):
        c += int(car[i][2])
    print(int(c // len(car)))
    return int(c // len(car))

def Horsepower_average(car):
    c = 0
    for i in range(len(car)):
        c += float(car[i][4])
    print(int(c // len(car)))
    return int(c // len(car))

def Light_cars(car):
    weights = []
    names = []
    for i in range(len(car)):
        weights.append(float(car[i][5]))
    weights.sort()
    for i in range(0, 50):
        for j in range(len(car)):
            if float(car[j][5]) == weights[i]:
                x = car[j][0], weights[i]
                names.append(x)
    print(show(names))
    return(names)

data = {"Japan_cars":japan_cars(car) ,
        "shortest_cars_name":small_name(car),
        "longest_carS_name":longe_name(car),
        "cylinders_average":Cylinders_average(car),
        "horsepower_average":Horsepower_average(car),
        "light_cars":Light_cars(car)
        }
with open("cars_dataset.json", "w") as f:
    json.dump(data, f)