import mysql.connector

conn = mysql.connector.connect(
    host="mysql_server",
    port=3308,
    user="lucas",
    password="lucastfg",
    database="safedata"
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES;")
print(cursor.fetchall())
conn.close()
