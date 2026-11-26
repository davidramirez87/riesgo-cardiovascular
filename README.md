# Calculadora de Riesgo Cardiovascular

Aplicación web en Flask que estima un nivel de riesgo cardiovascular básico a partir de género, edad, estatura y peso (IMC).

## Estructura

```
riesgo-cardiovascular/
├── app_riesgo.py        # Servidor Flask (rutas /, /evaluar y /health)
├── calculos.py          # Lógica del cálculo de riesgo
├── templates/
│   └── index.html       # Interfaz (Flask la busca en la carpeta templates/)
├── requirements.txt     # Dependencias: Flask y Gunicorn
├── render.yaml          # Configuración de despliegue en Render
├── .python-version      # Versión de Python
└── .gitignore
```

## Probar en local

```bash
python -m venv venv
# Windows: venv\Scripts\activate   |   Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python app_riesgo.py
```

Abre http://localhost:5000

## Subir a GitHub

1. Crea un repositorio nuevo y vacío en https://github.com/new (sin README).
2. Dentro de esta carpeta:

```bash
git init
git add .
git commit -m "Primera versión de la calculadora"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/riesgo-cardiovascular.git
git push -u origin main
```

## Desplegar en Render

**Opción A – Blueprint (usa `render.yaml`, recomendado)**

1. Entra a https://dashboard.render.com e inicia sesión con GitHub.
2. **New → Blueprint** y elige tu repositorio.
3. Render lee `render.yaml` y crea el servicio. Pulsa **Apply**.

**Opción B – Web Service manual**

1. **New → Web Service** y elige tu repositorio.
2. Configura:
   - Runtime: **Python 3**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app_riesgo:app --bind 0.0.0.0:$PORT`
   - Instance Type: **Free**
3. Pulsa **Create Web Service**.

Cuando el log muestre *Your service is live*, abre la URL `https://riesgo-cardiovascular-xxxx.onrender.com`.

Cada `git push` a `main` vuelve a desplegar automáticamente.

## Notas

- En el plan gratuito el servicio se "duerme" tras ~15 minutos sin uso; la primera visita después puede tardar cerca de un minuto.
- Puedes comprobar que el servidor está vivo en `/health`.
- La estimación es orientativa y no sustituye una evaluación médica.
