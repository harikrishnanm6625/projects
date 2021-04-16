import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="mydb"
)
cursor=db.cursor()
sql="update employee set salary=30000 where eid=100"
try:
    cursor.execute(sql)
    db.commit()  #to commit your changes in database
except Exception as e:
    print(e.args)
    db.rollback()   #not to store incomplete details and to rollback to initial
finally:
    db.close()

