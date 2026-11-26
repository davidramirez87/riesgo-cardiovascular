import os

from flask import Flask, render_template, request, jsonify
from calculos import evaluar_riesgo_cardiovascular

app = Flask(__name__)


# Ruta 1: Entrega la interfaz visual
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# Ruta de salud: Render la usa para saber si el servicio está vivo
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


# Ruta 2: API que recibe JSON, ejecuta el cálculo y devuelve JSON
@app.route("/evaluar", methods=["POST"])
def evaluar():
    # silent=True evita que Flask devuelva una página HTML de error
    # si el cuerpo no es JSON; así el frontend siempre recibe JSON.
    datos = request.get_json(silent=True)

    if not datos:
        return jsonify({"error": "No se recibieron datos válidos"}), 400

    try:
        genero = str(datos.get("genero", "")).upper()
        edad = int(datos.get("edad"))
        estatura = float(datos.get("estatura"))
        peso = float(datos.get("peso"))
    except (ValueError, TypeError):
        return jsonify({"error": "Verifica que los valores numéricos sean correctos"}), 400

    # Validación en el servidor (la del navegador se puede saltar)
    if genero not in ("M", "F"):
        return jsonify({"error": "El género debe ser 'M' o 'F'"}), 400
    if not 18 <= edad <= 120:
        return jsonify({"error": "La edad debe estar entre 18 y 120 años"}), 400
    if not 100 <= estatura <= 250:
        return jsonify({"error": "La estatura debe estar entre 100 y 250 cm"}), 400
    if not 30 <= peso <= 300:
        return jsonify({"error": "El peso debe estar entre 30 y 300 kg"}), 400

    resultado = evaluar_riesgo_cardiovascular(genero, edad, estatura, peso)
    return jsonify(resultado), 200


if __name__ == "__main__":
    # Solo para desarrollo local. En Render la app la arranca Gunicorn.
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto, debug=os.environ.get("FLASK_DEBUG") == "1")
