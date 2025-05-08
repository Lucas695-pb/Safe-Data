import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar el .env
dotenv_path = Path(__file__).resolve().parent.parent / "docker" / ".env"
load_dotenv(dotenv_path=dotenv_path)

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql_server"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER") or os.getenv("MYSQL_USER"),
        password=os.getenv("DB_PASSWORD") or os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("DB_NAME") or os.getenv("MYSQL_DATABASE")
    )
