# CQuest — Aprende a programar en C jugando

CQuest es una aplicación web educativa gamificada para aprender programación en C desde cero, pensada para niños de 12 años.

El sistema combina:
- Gamificación tipo Duolingo
- Editor tipo Visual Studio Code en el navegador
- Tutor IA que ayuda al alumno
- Ejecución segura de código C en Docker

---

## REQUISITOS PREVIOS

### 1. Docker Desktop
Descárgalo e instálalo desde:
https://www.docker.com/products/docker-desktop/

Ábrelo y espera a que el icono de la ballena aparezca estable en la barra superior antes de continuar.

### 2. Clave de OpenAI
La aplicación necesita una clave de OpenAI para el tutor IA.

Consíguela en: https://platform.openai.com/api-keys

Crea el archivo `.env` en la raíz del proyecto con este contenido:

```
OPENAI_API_KEY=sk-...tu-clave-aqui...
```

---

## CÓMO ARRANCAR LA APLICACIÓN

### Opción A — Doble clic (recomendada)

Haz doble clic en el archivo `iniciar.command` desde el Finder.

La primera vez puede tardar 3-5 minutos mientras se construyen las imágenes Docker.
Cuando termine, el navegador se abre automáticamente en http://localhost:3000

### Opción B — Terminal

```bash
cd /ruta/al/proyecto/CQuest_AppWeb
docker-compose up --build
```

Abre el navegador en http://localhost:3000

---

## CÓMO DETENER LA APLICACIÓN

Haz doble clic en `detener.command`, o ejecuta en la terminal:

```bash
docker-compose down
```

---

## PRIMERA VEZ

1. Haz clic en **Join Now** para crear tu cuenta
2. Introduce un nombre de usuario, email y contraseña
3. Empieza por el **World 1 — Hello World**

Los mundos se desbloquean completando todas las lecciones del mundo anterior:

| World | Tema          |
|-------|---------------|
| 1     | Hello World   |
| 2     | Variables     |
| 3     | If / Else     |
| 4     | Loops         |
| 5     | Functions     |
| 6     | Final Project |

---

## ESTRUCTURA DEL PROYECTO

```
/frontend          → Interfaz web (Next.js + React)
/backend           → API + ejecución de código (FastAPI + Python)
/docker-compose.yml
/iniciar.command   → Script de arranque para Mac
/detener.command   → Script de parada para Mac
.env               → Clave de OpenAI (debes crearlo tú)
```

---

## EJECUCIÓN DE CÓDIGO C

Cuando el alumno pulsa "Run":
1. El código se envía al backend
2. Se compila con GCC dentro del contenedor Docker
3. Se ejecuta con límite de 3 segundos
4. El resultado se devuelve al navegador

---

## SOLUCIÓN DE PROBLEMAS

**Error al arrancar Docker / timeout descargando imágenes**
- Abre Docker Desktop → Settings → Docker Engine
- Añade el mirror de registro:
```json
{
  "registry-mirrors": ["https://mirror.gcr.io"]
}
```
- Haz clic en Apply & Restart

**El tutor IA no funciona**
- Verifica que el archivo `.env` existe en la raíz del proyecto
- Comprueba que tu clave de OpenAI tiene créditos disponibles en platform.openai.com → Billing

**World 2 aparece bloqueado después de completar World 1**
- Cierra sesión y vuelve a entrar
