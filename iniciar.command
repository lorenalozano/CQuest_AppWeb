#!/bin/bash

# Ir a la carpeta del proyecto
cd "$(dirname "$0")"

# Añadir rutas donde Docker instala sus herramientas
export PATH="$PATH:/usr/local/bin:/opt/homebrew/bin:/Applications/Docker.app/Contents/Resources/bin"

clear
echo ""
echo "  ██████╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗"
echo " ██╔════╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝"
echo " ██║     ██║   ██║██║   ██║█████╗  ███████╗   ██║   "
echo " ██║     ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   "
echo " ╚██████╗╚██████╔╝╚██████╔╝███████╗███████║   ██║   "
echo "  ╚═════╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   "
echo ""
echo "  🎮 Aprende C programando como un héroe!"
echo ""
echo "─────────────────────────────────────────────────────"

# Verificar que Docker Desktop esté instalado
if [ ! -d "/Applications/Docker.app" ]; then
    echo ""
    echo "  ❌ Docker no está instalado."
    echo "  👉 Descárgalo en: https://www.docker.com/products/docker-desktop"
    echo ""
    read -p "  Presiona Enter para cerrar..."
    exit 1
fi

# Abrir Docker Desktop si no está corriendo
if ! docker info &> /dev/null; then
    echo ""
    echo "  🐳 Abriendo Docker Desktop..."
    open -a Docker
    echo ""
    echo "  ⏳ Esperando que Docker arranque (puede tardar ~30 segundos)..."
    printf "  "
    for i in {1..60}; do
        sleep 2
        if docker info &> /dev/null; then
            echo ""
            echo "  ✅ Docker está listo!"
            break
        fi
        printf "."
        if [ $i -eq 60 ]; then
            echo ""
            echo ""
            echo "  ❌ Docker tardó demasiado en arrancar."
            echo "  Asegúrate de que Docker Desktop está abierto (icono 🐳 en la barra superior)"
            echo "  y vuelve a hacer doble clic en iniciar.command"
            echo ""
            read -p "  Presiona Enter para cerrar..."
            exit 1
        fi
    done
fi

echo ""
echo "  🔨 Preparando CQuest..."
echo "  (la primera vez puede tardar 3-5 minutos, ten paciencia)"
echo ""

# Construir y arrancar en segundo plano
docker-compose up --build -d

if [ $? -ne 0 ]; then
    echo ""
    echo "  ❌ Hubo un error al iniciar CQuest."
    echo "  Intenta cerrar y volver a abrir Docker Desktop."
    echo ""
    read -p "  Presiona Enter para cerrar..."
    exit 1
fi

# Esperar a que el backend responda
echo ""
echo "  ⏳ Esperando que la app esté lista..."
printf "  "
for i in {1..30}; do
    sleep 2
    if curl -s http://localhost:8000/health > /dev/null 2>&1; then
        echo ""
        break
    fi
    printf "."
done

echo ""
echo "─────────────────────────────────────────────────────"
echo ""
echo "  ✅ ¡CQuest está listo!"
echo ""
echo "  🌐 Abriendo en el navegador..."
echo ""

sleep 1
open http://localhost:3000

echo "─────────────────────────────────────────────────────"
echo ""
echo "  👋 Para cerrar CQuest, haz doble clic en 'detener.command'"
echo "  🔒 No cierres esta ventana mientras juegas"
echo ""
echo "  Presiona Ctrl+C para detener desde aquí"
echo ""

docker-compose logs -f --tail=0
