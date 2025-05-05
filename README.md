# Safe Data - Plataforma de Ciberseguridad y Almacenamiento

Este proyecto despliega un entorno de servicios Docker destinados a gestionar almacenamiento, realizar operaciones web y facilitar análisis de ciberseguridad.

## 🔧 Servicios Incluidos

- 📦 **Nextcloud**: Plataforma de almacenamiento en la nube.
- 🐬 **MariaDB**: Base de datos relacional para usuarios, mensajes y eventos.
- 🧮 **phpMyAdmin**: Interfaz gráfica para gestionar la base de datos.
- 🌐 **Frontend Web**: Interfaz en HTML/CSS/JS servida con Apache.
- ⚙️ **FastAPI**: API REST para login, registro, formularios y eventos.
- 🧠 **CyberChef**: Herramienta web para análisis forense y decodificación.
- 🎯 **OWASP Juice Shop**: Aplicación vulnerable para prácticas de hacking ético.
- 🚀 **Redis**: Cache y soporte de sesión en memoria.
- 🔁 **Nginx**: Proxy reverso que enruta a la API.
- 🖥️ **Apache HTTP Server**: Sirve el frontend HTML estático.
- 🖼️ **Portainer**: Gestión visual avanzada de contenedores Docker.
- ♻️ **Backup Manager**: Crea copias de seguridad al iniciar el entorno.
- 🛡️ **ClamAV**: Escaneo antivirus periódico de archivos de Nextcloud.
- 📊 **Registro de Eventos**: Almacena actividades clave como inicio de sesión.

## 📁 Estructura del Proyecto

```
/docker-safe-data
│
├── backend/              # Backend con FastAPI (Python)
├── config/               # Archivos de configuración (Traefik, SSL, etc.)
├── docker/               # Dockerfile y docker-compose.yml
├── html/                 # Archivos del entorno Nextcloud
├── scripts/              # Scripts de conexión o inicialización
├── volumes/              # Volúmenes persistentes de Nextcloud y MariaDB
├── web/                  # Frontend web en HTML, CSS y JS
└── README.md             # Este archivo
```

## 🚀 Despliegue del Entorno

1. Asegúrate de tener Docker y Docker Compose instalados.
2. Abre una terminal y navega al directorio `docker-safe-data/docker`.
3. Ejecuta:

```bash
docker-compose up -d
```

Esto desplegará todos los contenedores: base de datos, phpMyAdmin, Nextcloud, FastAPI y opcionales como OWASP Juice Shop o CyberChef si están definidos.

## 🌐 Acceso a los Servicios

| Servicio         | URL                          | Puerto |
|------------------|-------------------------------|--------|
| Aplicación Web   | http://localhost:9090         | 9090   |
| phpMyAdmin       | http://localhost:8083         | 8083   |
| Nextcloud        | http://localhost:8084         | 8084   |
| OWASP Juice Shop | http://localhost:7000         | 7000   |
| CyberChef        | http://localhost:7001         | 7001   |

## 🛡️ Base de Datos

- **Gestión de usuarios**: Registro e inicio de sesión desde la web.
- **Formulario de contacto**: Los mensajes se almacenan en la tabla `contacto`.
- Registro de eventos (login, intentos, etc). 

Estructura esperada:

```sql
CREATE TABLE contacto (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  email VARCHAR(100),
  mensaje TEXT
);

CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100),
  email VARCHAR(100),
  password VARCHAR(100)
);

CREATE TABLE eventos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  tipo_evento VARCHAR(50),
  usuario VARCHAR(100),
  fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

🧠 Funcionalidades Avanzadas
🔁 Backups automáticos de volúmenes cada vez que se inicia el entorno.

🧪 CyberChef para decodificación, análisis binario, hashing, etc.

🛡️ ClamAV escanea archivos en /nextcloud cada hora.

📊 Registro de eventos: log de actividades como login, ataques, etc.

👨‍💻 Portainer: panel de control de contenedores, volúmenes, redes y más.

🐱‍💻 Ciberseguridad desde Kali Linux
Puedes lanzar ataques éticos desde Kali Linux sobre este entorno:

🔍 Escaneo: nmap, nikto, gobuster, wpscan, etc.

💣 Explotación: Metasploit, msfvenom.

🔐 Cracking: Hydra, John The Ripper.

🧬 Forense: Autopsy, bulk_extractor.

🚨 IDS/IPS: Snort, Suricata.

🧾 Auditoría: Lynis.

📦 Variables y Seguridad
Las contraseñas y variables sensibles están almacenadas en .env, que no se sube al repositorio (.gitignore lo bloquea).

Puedes usar .env.example para clonar el proyecto sin comprometer datos.

## 👨‍💻 Contribuir

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b mi-contribucion`).
3. Realiza tus cambios y haz commit.
4. Haz push a tu rama (`git push origin mi-contribucion`).
5. Abre un Pull Request en GitHub.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.
