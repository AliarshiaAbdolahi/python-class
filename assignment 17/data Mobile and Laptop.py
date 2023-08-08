import sqlite3

connection = sqlite3.connect("My data.db")
c = connection.cursor()

c.execute("""
    CREATE TABLE Mobile (
          Brand TEXT, 
          Name TEXT,
          Year TEXT,
          Camera TEXT,
          Ram TEXT,
          Price TEXT 
    )
""")

c.execute("""
    CREATE TABLE Laptop (
          Brand TEXT, 
          Name TEXT,
          CPU TEXT,
          Ram TEXT,
          HDD TEXT,
          SDD TEXT,
          OS TEXT
    )
""")

many_mobile = [
    ("Xiaomi", "Poco X3 NFC", "2020", "108MP", "8", "6.349.000"),
    ("samsung", "Galaxy A53", "2022", "64MP", "8", "12.259.000"),
    ("Apple", "Iphone 11", "2019", "12MP", "4", "12.750.000")
    ("Xiaomi", "Redmi Note 9", "2020", "48MP", "4", "5.999.000")
    ("samsung", "Galaxy A23", "2022", "50MP", "6", "7.020.000")
    ("Apple", "Iphone X", "2017", "12MP", "3", "14.500.000")
    ("Xiaomi", "Redmi Note 7", "2019", "48MP", "4", "2.700.000")
]
c.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?)", many_mobile)

many_laptop = [
    ("Apple", "MacBookAir M2", "Apple M2", "8", "❌", "✔", "MAC")
    ("ASUS", "VivoBook R565EP", "intel core i5-1153G7", "8", "❌", "✔", "Windows")
    ("ASUS", "VivoBook Pro 14X", "core i7-11370H", "16", "❌", "✔", "Windows")
    ("Samsung", "Notebook 9 Pen", "intel core i7", "8", "❌", "✔", "Windows")
    ("Xiaomi", "Mi Notebook Pro 14", "core i7-1130H", "16", "❌", "✔", "Windows")
]
c.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?)", many_laptop)

c.execute("SELECT * FROM Mobile WHERE Year < 3")
item = c.fetchall()
for i in item:
    print(item)

c.execute("DELETE FROM Laptop WHERE CPU <= 3")
item = c.fetchall()
for i in item:
    print(item)

c.execute("SELECT * FROM Mobile WHERE Price > 50000000")
item = c.fetchall()
for i in item:
    print(item)

