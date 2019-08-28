import mysql.connector


def select_data():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="8561312",
	  database="stock"
	)

	db = mydb.cursor()
	db.execute("SELECT * FROM stock.stock")

	myresult = db.fetchall()

	for x in myresult:
  		print(x)
