import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="mydb",
    passwd="Password@123",
)
cursor=db.cursor()
sql=("insert into employee(eid,name,dept,salary)values(106,'jithin','mrkt',70000)")
try:
    cursor.execute(sql)
    db.commit()  #to commit your changes in database
except Exception as e:
    print(e.args)
    db.rollback()   #not to store incomplete details and to rollback to initial
finally:
    db.close()
