from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar .env manualmente si se ejecuta por separado
dotenv_path = Path(__file__).resolve().parent.parent / "docker" / ".env"
load_dotenv(dotenv_path=dotenv_path)

DB_HOST = os.getenv("DB_HOST", "mysql_server")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER") or os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD") or os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("DB_NAME") or os.getenv("MYSQL_DATABASE")

router = APIRouter()

class Notificacion(BaseModel):
    usuario_id: int
    mensaje: str

@router.post("/api/notificaciones")
def nueva_notificacion(notif: Notificacion):
    try:
        db = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO notificaciones (usuario_id, mensaje, leido, fecha) VALUES (%s, %s, %s, %s)",
            (notif.usuario_id, notif.mensaje, False, datetime.now())
        )
        db.commit()
        cursor.close()
        db.close()
        return {"message": "Notificación creada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/notificaciones/{usuario_id}")
def obtener_notificaciones(usuario_id: int):
    try:
        db = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM notificaciones WHERE usuario_id = %s ORDER BY fecha DESC", (usuario_id,))
        notifs = cursor.fetchall()
        cursor.close()
        db.close()
        return notifs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/api/notificaciones/leida/{notificacion_id}")
def marcar_leida(notificacion_id: int):
    try:
        db = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = db.cursor()
        cursor.execute("UPDATE notificaciones SET leido = TRUE WHERE id = %s", (notificacion_id,))
        db.commit()
        cursor.close()
        db.close()
        return {"message": "Notificación marcada como leída"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
