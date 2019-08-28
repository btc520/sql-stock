import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="8561312",
  database="stock"
)

# print(mydb)

db = mydb.cursor()

#db.execute("use test")

db.execute("select * from stock;")
myresult = db.fetchall()

#db.execute("SHOW DATABASES")

for x in myresult:
        print(x)



