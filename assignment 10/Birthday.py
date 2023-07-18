import datetime

day_of_person = int(input("in what day were you born: "))
month_of_person = int(input("in what month were you born: "))
year_of_person = int(input("in what yaer were you born: "))

now = datetime.datetime.today()
now_year = int(now.year)

age = now_year - year_of_person

print(f"You are {age} years old \n")

day = age * 365
week = age * 52        # (hafte ro be tor taghribi hesab kardam)
second = age * 31536000

print(f"You lived for {second} seconds \n")
print(f"Ypu lived for {week} weeks \n")
print(f"You lived for {day} days \n")