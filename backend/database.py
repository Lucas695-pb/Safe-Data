import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="db",
        user="lucas",
        password="lucastfg",
        database="safedata"
    )
