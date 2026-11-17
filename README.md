# Safe Data - Plataforma de Ciberseguridad y Almacenamiento

Este proyecto despliega un entorno completo basado en Docker que integra múltiples servicios orientados a la gestión de almacenamiento, operación de aplicaciones web y análisis de ciberseguridad.

Gracias al uso de contenedores, cada componente del sistema se encuentra aislado, es fácilmente replicable y escalable. Incluye una plataforma cloud privada (Nextcloud), una API desarrollada en FastAPI para gestión de usuarios, formularios y seguridad, un sistema de base de datos relacional (MariaDB), y un panel de administración visual (phpMyAdmin y Portainer).

Adicionalmente, incorpora herramientas avanzadas de análisis forense (CyberChef), pruebas de hacking ético (OWASP Juice Shop), escaneo antivirus automatizado (ClamAV) y backups programados, lo que lo convierte en un entorno versátil tanto para producción como para prácticas educativas, auditorías o pruebas en ciberseguridad. Todo ello está centralizado en una arquitectura coherente y controlada mediante un único archivo docker-compose.

## 🔧 Servicios Incluidos

-  **Nextcloud**: Plataforma de almacenamiento en la nube.
-  **MariaDB**: Base de datos relacional para usuarios, mensajes y eventos.
-  **phpMyAdmin**: Interfaz gráfica para gestionar la base de datos.
-  **Frontend Web**: Interfaz en HTML/CSS/JS servida con Apache.
-  **FastAPI**: API REST para login, registro, formularios y eventos.
-  **CyberChef**: Herramienta web para análisis forense y decodificación.
-  **OWASP Juice Shop**: Aplicación vulnerable para prácticas de hacking ético.
-  **Redis**: Cache y soporte de sesión en memoria.
-  **Nginx**: Proxy reverso que enruta a la API.
-  **Apache HTTP Server**: Sirve el frontend HTML estático.
-  **Portainer**: Gestión visual avanzada de contenedores Docker.
-  **Backup Manager**: Crea copias de seguridad al iniciar el entorno.
-  **ClamAV**: Escaneo antivirus periódico de archivos de Nextcloud.
-  **Registro de Eventos**: Almacena actividades clave como inicio de sesión..

##  Estructura del Proyecto

```
/docker-safe-data
│
├── backend/              # Backend FastAPI (Python)
├── docker/               # Dockerfile y docker-compose.yml
├── config/               # Directorio para ciertos archivos de configuración
├── scripts/              # Archivos adicionales (verificar_entorno.sh, database-connection) 
├── volumes/              # Volúmenes persistentes (db, nextcloud, backups, clamav, portainer)
├── web/                  # Frontend web en HTML, CSS y JS
└── README.md             # Este archivo
```

##  Despliegue del Entorno

1. Asegúrate de tener Docker y Docker Compose instalados.
2. Abre una terminal y navega al directorio `docker-safe-data/docker`.
3. Ejecuta:

```bash
docker-compose up -d --build
```

Esto desplegará todos los contenedores definidos, incluyendo base de datos, phpMyAdmin, Nextcloud, FastAPI, Redis, Portainer, Nginx, etc.

##  Acceso a los Servicios

| Servicio         | URL                          | Puerto |
|------------------|-------------------------------|--------|
| Aplicación Web   | http://localhost:9090         | 9090   |
| phpMyAdmin       | http://localhost:8083         | 8083   |
| Nextcloud        | http://localhost:8084         | 8084   |
| OWASP Juice Shop | http://localhost:7001         | 7001   |
| CyberChef        | http://localhost:7002         | 7002   |
| Portainer        | https://localhost:9443        | 9443   |

##  Base de Datos

-  Registro e inicio de sesión desde la web.
-  Formulario de contacto que almacena los mensajes.
-  Registro de eventos (login, intentos, etc).

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

##  Funcionalidades de Seguridad y Gestión

-  **Backups Automáticos**: Se realiza una copia comprimida diaria de la base de datos y Nextcloud.
-  **Escaneo Antivirus**: ClamAV escanea automáticamente los archivos subidos a Nextcloud cada hora.
-  **Análisis Forense con CyberChef**: Disponible para pruebas con cadenas, codificaciones, etc.
-  **Gestión Visual**: Portainer permite administrar contenedores, volúmenes, logs y tareas programadas.

##  Ciberseguridad con Kali Linux

Desde Kali Linux se puede interactuar con el entorno para realizar pruebas de ciberseguridad:

-  **Análisis de tráfico**: Con herramientas como Wireshark.
-  **Análisis de vulnerabilidades automatizado**: Con herramientas como `nmap`, `nikto`, `OpenVAS`, etc.
-  **Forense**: Con Autopsy.
-  **Exploits**: Uso de Metasploit y scripts personalizados.
-  **Cracking de contraseñas**: Herramientas como Hydra o John The Ripper.
-  **Escaneo Web**: WPScan, dirb, gobuster, etc.
-  **IDS/IPS**: Implementación de Snort o Suricata para detección de intrusos.
-  **Auditorías**: Análisis del sistema con Lynis.

##  Variables y Seguridad

Las contraseñas y variables sensibles están almacenadas en .env, que no se sube al repositorio (.gitignore lo bloquea).

Puedes usar .env.example para clonar el proyecto sin comprometer datos.

##  Contribuir

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b mi-contribucion`).
3. Realiza tus cambios y haz commit.
4. Haz push a tu rama (`git push origin mi-contribucion`).
5. Abre un Pull Request en GitHub.

##  Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.+
