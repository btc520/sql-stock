import mysql.connector
import time
from sel import select_data



now = time.strftime('%Y-%m-%d')

name = raw_input ("1. name?:   ")
price = raw_input ("2. price?:   ")
share = raw_input ("3. share:   ")
date3 = raw_input("4. date? e.g.19860224:   ")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="8561312",
  database="stock"
)

db = mydb.cursor()


sql = "INSERT INTO stock (name, date2, share, price) values (%s, %s, %s, %s)"

if date3 == "":
        print("empty data use now")
	val = (name, now, share, price )
else:
	val = (name, date3, share, price )

db.execute(sql, val)

mydb.commit()

select_data()
