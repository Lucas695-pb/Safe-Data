# Safe Data - Plataforma de Ciberseguridad y Almacenamiento

Este proyecto despliega un entorno de servicios Docker destinados a gestionar almacenamiento, realizar operaciones web y facilitar análisis de ciberseguridad.

## 🔧 Servicios Incluidos

- **Nextcloud**: Plataforma de almacenamiento en la nube.
- **MariaDB**: Base de datos relacional usada para el backend.
- **phpMyAdmin**: Interfaz web para la gestión de bases de datos.
- **Aplicación Web**: HTML + FastAPI para la interacción del usuario.
- **FastAPI (Python)**: Backend ligero para la API REST.
- **CyberChef (Opcional)**: Herramienta web para análisis forense y decodificación.
- **OWASP Juice Shop (Opcional)**: Aplicación vulnerable para prácticas de hacking ético.

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
```

## ⚙️ Variables Importantes

Configuradas en el archivo `docker-compose.yml`:

- `MYSQL_ROOT_PASSWORD=lucastfg`
- `MYSQL_DATABASE=safedata`
- `MYSQL_USER=lucas`
- `MYSQL_PASSWORD=lucastfg`

## 👨‍💻 Contribuir

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b mi-contribucion`).
3. Realiza tus cambios y haz commit.
4. Haz push a tu rama (`git push origin mi-contribucion`).
5. Abre un Pull Request en GitHub.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.
