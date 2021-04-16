import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="mydb",
    passwd="Password@123",
)
cursor = db.cursor()
f=open("/home/harikrishnan/PycharmProjects/advancedpython/pythontomysql/employee","r")
for lines in f:
    data=lines.rstrip("\n").split(",")   #102,ram,developer,26500
    sql = "insert into employee(eid,name,dept,salary) values(%s,%s,%s,%s)" #data comes from file as string so %s
    try:    #we get the data as list so we have to convert to tuple
        cursor.execute(sql,tuple(data))  #transfer data as tuple
        db.commit()
    except Exception as e:
        print(e.args)
        db.rollback()

db.close()



