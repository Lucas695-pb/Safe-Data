FROM python:3.11-slim

WORKDIR /app

# Copia los archivos del backend
COPY ../backend /app

# Instala las dependencias del requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9090

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9090"]
