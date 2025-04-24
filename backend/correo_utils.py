import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def enviar_correo_gmail(destino, asunto, cuerpo):
    remitente = "lukpb17@gmail.com"
    password = "lucastfg"

    mensaje = MIMEMultipart()
    mensaje["From"] = str(Header(remitente, 'utf-8'))
    mensaje["To"] = str(Header(destino, 'utf-8'))
    mensaje["Subject"] = Header(asunto, 'utf-8')

    mensaje.attach(MIMEText(cuerpo, "plain", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()
        servidor.login(remitente, password)
        servidor.send_message(mensaje)
