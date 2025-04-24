#!/bin/bash

echo "🔍 Verificación del entorno Safe Data tras actualización..."

# Comprobar si Docker está corriendo
echo -n "🛠️  Comprobando si Docker está corriendo... "
if ! docker info >/dev/null 2>&1; then
  echo "❌ Docker no está corriendo"
  exit 1
else
  echo "✅ OK"
fi

# Mostrar contenedores activos
echo "📦 Contenedores activos..."
docker ps --format "table {{.Names}}\t{{.Status}}"

# Comprobar acceso a los volúmenes
echo -n "📁 Comprobando acceso a volúmenes... "
if [ -d "../volumes/db_data" ] && [ -d "../volumes/nextcloud_data" ]; then
  echo "✅ OK"
else
  echo "❌ Faltan volúmenes"
fi

# Probar si docker compose funciona correctamente
echo "🚀 Probando docker compose..."
if docker compose config >/dev/null 2>&1; then
  echo "✅ docker compose operativo"
else
  echo "❌ ERROR al ejecutar docker compose config"
fi

# Comprobación de puertos (servicios web)
echo "🌐 Verificando acceso web a servicios:"
puertos=(9090 8083 8084 7001 7002 9443)
for puerto in "${puertos[@]}"; do
  if nc -z localhost "$puerto"; then
    echo "✅ localhost:$puerto accesible"
  else
    echo "❌ localhost:$puerto no responde"
  fi
done

echo "🎉 Verificación finalizada."
