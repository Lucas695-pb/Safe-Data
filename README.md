Safe Data - Plataforma de Ciberseguridad y Almacenamiento

Safe Data es un entorno completo y modular basado en Docker, diseñado para ofrecer una solución integral en almacenamiento privado, gestión web segura y auditorías de ciberseguridad. Reúne herramientas modernas para administración de sistemas, pruebas de seguridad ofensiva y defensiva, y desarrollo web.

Gracias al uso de contenedores Docker, cada componente está aislado, es fácilmente replicable, actualizable y escalable. El sistema combina almacenamiento cloud, gestión web segura, APIs personalizadas y múltiples utilidades orientadas a la formación, pruebas o entornos productivos.

🚀 Características Principales

📁 Almacenamiento privado con Nextcloud.

🔐 Gestión de usuarios con FastAPI, formularios web y notificaciones.

🐬 Base de datos relacional MariaDB, con interfaz gráfica en phpMyAdmin.

🌐 Frontend web estático (HTML/CSS/JS) servido con Apache.

⚖️ Gestión avanzada de contenedores con Portainer.

🧠 Análisis forense con CyberChef.

🎯 Pruebas de hacking ético con OWASP Juice Shop.

🛡️ Escaneo antivirus automático con ClamAV.

♻️ Sistema de backups automáticos programados.

🔀 Gestión de sesiones y rendimiento con Redis y Nginx.

📦 Servicios Incluidos

Servicio

Descripción

Nextcloud

Almacenamiento en la nube privado

MariaDB

Base de datos relacional

phpMyAdmin

Interfaz gráfica para MariaDB

FastAPI

API RESTful: login, registro, contacto, notificaciones

Apache

Servidor para frontend HTML/CSS/JS

Redis

Cache/sesiones

Nginx

Proxy reverso para la API

Portainer

Panel de administración de contenedores

CyberChef

Herramienta para análisis forense

Juice Shop

Aplicación vulnerable para prácticas de seguridad

ClamAV

Escáner antivirus automatizado

Backup Manager

Creador de copias de seguridad comprimidas

📁 Estructura del Proyecto

/docker-safe-data
│
├── backend/              # Backend FastAPI (Python)
├── docker/               # Dockerfile y docker-compose.yml
├── config/               # Archivos de configuración
├── scripts/              # Scripts auxiliares (ej. verificar_entorno.sh)
├── volumes/              # Datos persistentes (db, nextcloud, clamav, etc.)
├── web/                  # Sitio web HTML/CSS/JS
└── README.md             # Este archivo

🔧 Despliegue del Entorno

Instala Docker y Docker Compose.

Ve al directorio del entorno:

cd docker-safe-data/docker

Ejecuta:

docker-compose up -d --build

Esto desplegará toda la infraestructura en contenedores.

🌐 Acceso a los Servicios

Servicio

URL

Puerto

Web Frontend

http://localhost:9090

9090

phpMyAdmin

http://localhost:8083

8083

Nextcloud

http://localhost:8084

8084

Juice Shop

http://localhost:7001

7001

CyberChef

http://localhost:7002

7002

Portainer

https://localhost:9443

9443

🗃️ Base de Datos

Tablas principales:

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
  password VARCHAR(100),
  ultimo_login DATETIME
);

CREATE TABLE eventos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  tipo_evento VARCHAR(50),
  usuario VARCHAR(100),
  fecha_hora DATETIME
);

CREATE TABLE notificaciones (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT,
  mensaje TEXT,
  leido BOOLEAN DEFAULT FALSE,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

🧠 Funcionalidades Avanzadas

📩 Notificaciones personalizadas tras eventos como registro o login.

📋 Registro de eventos: login, formularios, actividad de usuarios.

🔀 Backups automáticos de la base de datos y archivos.

🛡️ Escaneo antivirus periódico (ClamAV sobre Nextcloud).

⚖️ Panel gráfico de administración con Portainer.

🔍 Pruebas y análisis forense vía CyberChef y herramientas externas.

🐱‍💻 Ciberseguridad con Kali Linux

Este entorno permite conectarse desde Kali Linux para pruebas ofensivas:

🔎 Análisis de tráfico con Wireshark

🔐 Enumeración con Nmap, Nikto, Gobuster, etc.

💣 Uso de exploits (Metasploit, CVEs, etc.)

🔍 Análisis forense (Autopsy)

🚨 IDS con Snort o Suricata

🧞 Auditorías con Lynis

🔐 Seguridad y Variables

Las variables sensibles (usuarios, contraseñas) están en .env, que está en .gitignore.

El archivo .env.example permite clonar el entorno sin comprometer datos reales.

👨‍💼 Contribuciones

Haz fork del repo

Crea una rama: git checkout -b mi-cambio

Haz commit: git commit -m "Mi mejora"

Push: git push origin mi-cambio

Abre un Pull Request en GitHub

📄 Licencia

Este proyecto está bajo la Licencia MIT.

Desarrollado con ❤️ por Lucas Parreño y colaboradores.
