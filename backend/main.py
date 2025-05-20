from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import mysql.connector
from dotenv import load_dotenv
import os
from datetime import datetime
from notificaciones import router as notificaciones_router

dotenv_path = Path(__file__).resolve().parent.parent / "docker" / ".env"
load_dotenv(dotenv_path=dotenv_path)

DB_HOST = os.getenv("DB_HOST", "mysql_server")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER") or os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD") or os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("DB_NAME") or os.getenv("MYSQL_DATABASE")

app = FastAPI()
app.include_router(notificaciones_router)

BASE_DIR = Path(__file__).resolve().parent.parent
WEB_DIR = BASE_DIR / "web"

app.mount("/css", StaticFiles(directory=WEB_DIR / "css"), name="css")
app.mount("/js", StaticFiles(directory=WEB_DIR / "js"), name="js")
app.mount("/img", StaticFiles(directory=WEB_DIR / "img"), name="img")

@app.get("/", response_class=HTMLResponse)
async def get_index():
    return FileResponse(WEB_DIR / "index.html")

@app.get("/contacto", response_class=HTMLResponse)
async def contacto():
    return FileResponse(WEB_DIR / "contacto.html")

@app.get("/cuenta", response_class=HTMLResponse)
async def cuenta():
    return FileResponse(WEB_DIR / "cuenta.html")

@app.get("/servicios", response_class=HTMLResponse)
async def servicios():
    return FileResponse(WEB_DIR / "servicios.html")

@app.get("/cloud", response_class=HTMLResponse)
async def cloud():
    return FileResponse(WEB_DIR / "cloud.html")

def registrar_evento(evento: str, descripcion: str):
    try:
        db = mysql.connector.connect(
            host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
        )
        cursor = db.cursor()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(
            "INSERT INTO eventos (evento, descripcion, fecha_hora) VALUES (%s, %s, %s)",
            (evento, descripcion, timestamp)
        )
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print("❌ Error registrando evento:", e)

def crear_notificacion(usuario_id: int, mensaje: str = "Tu información se ha guardado con éxito."):
    try:
        db = mysql.connector.connect(
            host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
        )
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO notificaciones (usuario_id, mensaje, leido) VALUES (%s, %s, %s)",
            (usuario_id, mensaje, False)
        )
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print("❌ Error creando notificación:", e)

@app.post("/api/contacto")
async def contacto_post(nombre: str = Form(...), email: str = Form(...), mensaje: str = Form(...)):
    try:
        db = mysql.connector.connect(
            host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
        )
        cursor = db.cursor()
        cursor.execute("INSERT INTO contacto (nombre, email, mensaje) VALUES (%s, %s, %s)", (nombre, email, mensaje))
        db.commit()
        cursor.close()
        db.close()
        registrar_evento("Contacto", f"Mensaje de {nombre} ({email})")
        return JSONResponse(content={"message": "Mensaje recibido con éxito"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/api/register")
async def register(username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    try:
        db = mysql.connector.connect(
            host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
        )
        cursor = db.cursor()
        cursor.execute("INSERT INTO usuarios (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        usuario_id = cursor.lastrowid
        db.commit()
        cursor.close()
        db.close()
        registrar_evento("Registro", f"Nuevo usuario registrado: {username}")
        crear_notificacion(usuario_id)
        return JSONResponse(content={"message": "Registro exitoso"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/api/login")
async def login(login_username: str = Form(...), login_password: str = Form(...)):
    try:
        db = mysql.connector.connect(
            host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
        )
        cursor = db.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE username=%s AND password=%s", (login_username, login_password))
        user = cursor.fetchone()

        if user:
            usuario_id = user[0]
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("UPDATE usuarios SET ultimo_login=%s WHERE id=%s", (timestamp, usuario_id))
            db.commit()
            registrar_evento("Login", f"Inicio de sesión: {login_username}")
            crear_notificacion(usuario_id)
            cursor.close()
            db.close()
            return JSONResponse(content={"message": "Inicio de sesión exitoso", "usuario_id": usuario_id})
        else:
            cursor.close()
            db.close()
            return JSONResponse(status_code=401, content={"error": "Credenciales inválidas"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
