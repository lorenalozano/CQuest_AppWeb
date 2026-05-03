#!/bin/bash

cd "$(dirname "$0")"

export PATH="$PATH:/usr/local/bin:/opt/homebrew/bin:/Applications/Docker.app/Contents/Resources/bin"

clear
echo ""
echo "  🛑 Cerrando CQuest..."
echo ""

if ! docker info &> /dev/null; then
    echo "  ℹ️  Docker no está corriendo. No hay nada que detener."
else
    docker-compose down
    echo ""
    echo "  ✅ CQuest se ha cerrado correctamente."
fi

echo ""
echo "  👋 ¡Hasta la próxima aventura!"
echo ""
sleep 3
