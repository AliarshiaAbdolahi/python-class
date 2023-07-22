def Date(month,day,year):
    return f"{year}/{month}/{day}"

day = int(input("Please enter day: "))
month = int(input("Pleas enter month: "))
year = int(input("Please ener year: "))
print("Date: ",Date(month,day,year))
