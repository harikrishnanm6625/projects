import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="mydb",
    passwd="Password@123",
)
cursor=db.cursor()
sql=("create table employee(eid int,name varchar(50),dept varchar(50),salary int)")
cursor.execute(sql)
db.close()