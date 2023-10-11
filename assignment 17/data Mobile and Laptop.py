import sqlite3
import csv

laptops = []
with open("D:/python course/assignment 17/laptops.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        laptops.append(tuple(row))

connect = sqlite3.connect("mobileandlaptap.db")
data = connect.cursor() 
data.execute("""
    CREATE TABLE mobile (
            brand TEXT,
            name TEXT,
            year TEXT,
            ram TEXT,
            camera TEXT,
            price TEXT
    )
""")
data.execute("""
    CREATE TABLE laptop(
            Manufacturer TEXT,
            Brand TEXT,
            Category TEXT,
            Scrreen_Size TEXT,
            Screen TEXT,
            CPU TEXT,
            RAM TEXT,
            Storage TEXT,
            GPU TEXT,
            Op_System TEXT,
            Op_System_Version TEXT,
            Weight TEXT,
            Price TEXT
    )
""")
# mobile: brand, name, year, ram, camera, price
customers = [("Apple", "iPad Pro 12.9 (2018)", "2018", "4 GB", "12 MP", "1100 EUR"),
            ("Apple", "iPad Pro 11", "2018", "4 GB", "12 MP", "880 EUR"),
            ("Apple", "iPhone XS Max", "2018", "4 GB", "12 MP", "1250 EUR"),
            ("Apple", "iPhone XS", "2018", "4 GB", "12 MP", "1150 EUR"),
            ("Apple", "iPhone XR", "2018", "3 GB", "12 MP", "850 EUR"),
            ("Apple", "Watch Series 4", "2018", "0 GB", "No", "700 EUR"),
            ("Apple", "Watch Series 4 Aluminum", "2018", "0 GB", "No", "430 EUR"),
            ("Apple", "iPad 9.7 (2018)", "2018", "2 GB", "8 MP", "350 EUR")]

# add Phones
for i in customers:
    connect.execute("INSERT INTO mobile VALUES (?, ?, ?, ?, ?, ?)", i)
for i in laptops:
    connect.execute("INSERT INTO laptop VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", i)

data.execute("SELECT * FROM mobile WHERE year >= '2017'")
itames = data.fetchall()
for i in itames:
    print(i)
data.execute("DELETE FROM laptop WHERE RAM <= '4'")
data.execute("SELECT CPU FROM laptop WHERE RAM > '4'")
for i in data.fetchall():
    print(i)

print("___________________________________________")
data.execute("SELECT * FROM laptop ORDER BY RAM DESC")
items = data.fetchall()
c = 0
for i in items:
    print(i)
    c+=1
    if c == 5:
        break

data.execute("SELECT * FROM mobile WHERE Price > '500'")
for i in data.fetchall():
    print(i)

data.execute("SELECT * FROM laptop WHERE Price > '10000'")
for i in data.fetchall():
    print(i)


connect.commit()
connect.close()