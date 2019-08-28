from sel import select_data

import mysql.connector

from prettytable import PrettyTable

pt = PrettyTable()
pt.field_names = ["id", "name", "total share", "total cost", "avg. price"]

select_data()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="8561312",
  database="stock"
)

db = mydb.cursor()

sql_del = "drop table sum1"
	
db.execute(sql_del)

sql_new = " \
	CREATE TABLE sum1 \
	(id INT AUTO_INCREMENT PRIMARY KEY, \
	name VARCHAR(255), \
	total_share INT(100), \
	total_cost FLOAT(50,3), \
	avg_price FLOAT(50,3) \
	);"
db.execute(sql_new)		
 
sql_main = " \
	INSERT INTO sum1(name, total_share, total_cost, avg_price) \
	SELECT name, \
	SUM(share) 'total_share', \
	round(SUM(price * share),2) 'total_cost', \
	round(SUM(price * share)/SUM(share),2) 'avg_price' \
	FROM stock \
	GROUP BY name;"
db.execute(sql_main)

db.execute("SELECT * FROM stock.sum1")
myresult = db.fetchall()

for x in myresult:
	pt.add_row(x)

print(pt)