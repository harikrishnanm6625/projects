# mysql-connector
# #step1 import mysql module
# #step2 establish connection
# step3 create curser object
# #execute sql queries
# #close db connection
import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="pythonfeb",
    password="Password@123",
    #auth_plugin="mysql_native_password"-----FOR WINDOWS
)
cursor=db.cursor()
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
