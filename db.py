import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="V@m$h!@1212",
    database="testdb"
)
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id int AUTO_INCREMENT primary key,
            name varchar(50),
            age int
            )""")
#update table
cursor.execute("delete from users where id=%s",(6,))
conn.commit()
print("Done")
cursor.close()
conn.close()