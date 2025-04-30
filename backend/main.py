from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import mysql.connector
from dotenv import load_dotenv
import os

# Cargar variables del .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "mysql_server")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DATABASE")

app = FastAPI()

# Rutas
BASE_DIR = Path(__file__).resolve().parent.parent
WEB_DIR = BASE_DIR / "web"

# Montaje de rutas estáticas
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

# API Contacto
@app.post("/api/contacto")
async def contacto_post(nombre: str = Form(...), email: str = Form(...), mensaje: str = Form(...)):
    try:
        db = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = db.cursor()
        cursor.execute("INSERT INTO contacto (nombre, email, mensaje) VALUES (%s, %s, %s)", (nombre, email, mensaje))
        db.commit()
        cursor.close()
        db.close()
        print("📩 Mensaje recibido:", nombre, email, mensaje)
        return {"message": "Mensaje recibido con éxito"}
    except Exception as e:
        print("❌ Error en contacto:", e)
        return {"error": str(e)}

# API Registro
@app.post("/api/register")
async def register(username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    try:
        db = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = db.cursor()
        cursor.execute("INSERT INTO usuarios (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        db.commit()
        cursor.close()
        db.close()
        print("✅ Registro:", username, email)
        return {"message": "Registro exitoso"}
    except Exception as e:
        print("❌ Error en registro:", e)
        return {"error": str(e)}

# API Login
@app.post("/api/login")
async def login(login_username: str = Form(...), login_password: str = Form(...)):
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            port=3308,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username=%s AND password=%s", (login_username, login_password))
        user = cursor.fetchone()
        cursor.close()
        db.close()

        if user:
            print("🔐 Login:", login_username)
            return {"message": "Inicio de sesión exitoso"}
        else:
            return {"error": "Credenciales inválidas"}
    except Exception as e:
        print("❌ Error en login:", e)
        return {"error": str(e)}
