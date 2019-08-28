from sel import select_data

import mysql.connector

select_data()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="8561312",
  database="stock"
)

db = mydb.cursor()


type = raw_input("1. type of data to del e.g i for id, n for name, d for date, p for price, s for share:   ")
if type == 'i':
	id = raw_input("2. enter id:   ")
	sql = "DELETE FROM stock WHERE id = %s" % id
if type == 'n':
	name = raw_input("2. enter name:   ")
	sql = "DELETE FROM stock WHERE name = %s" % name
if type == 'd':
	date = raw_input("2. enter date:   ")
	sql = "DELETE FROM stock WHERE date = %s" % date
if type == 'p':
	price = raw_input("2. enter price:   ")
	sql = "DELETE FROM stock WHERE price = %s" % price
if type == 's':
	share = raw_input("2. enter share:   ")	
	sql = "DELETE FROM stock WHERE share = %s" % share
	
db.execute(sql)
mydb.commit()
	
select_data()
	