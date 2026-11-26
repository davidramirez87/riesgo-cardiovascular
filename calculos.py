def evaluar_riesgo_cardiovascular(genero: str, edad: int, estatura_cm: float, peso_kg: float) -> dict:
    """
    Evalúa una estimación básica de riesgo cardiovascular según variables antropométricas y demográficas.
    """
    # Convertir estatura a metros y calcular IMC
    estatura_m = estatura_cm / 100
    imc = round(peso_kg / (estatura_m ** 2), 2)

    puntos_riesgo = 0
    factores = []

    # 1. Evaluación por IMC
    if imc >= 30:
        puntos_riesgo += 3
        factores.append("Obesidad (IMC >= 30)")
    elif imc >= 25:
        puntos_riesgo += 1
        factores.append("Sobrepeso (IMC entre 25 y 29.9)")
    elif imc < 18.5:
        factores.append("Bajo peso (IMC < 18.5)")

    # 2. Evaluación por edad y género biológico
    genero = genero.upper()
    if genero == "M":
        if edad >= 55:
            puntos_riesgo += 3
            factores.append("Edad >= 55 años")
        elif edad >= 45:
            puntos_riesgo += 2
            factores.append("Edad de riesgo masculino (>= 45 años)")
    elif genero == "F":
        if edad >= 65:
            puntos_riesgo += 3
            factores.append("Edad >= 65 años")
        elif edad >= 55:
            puntos_riesgo += 2
            factores.append("Edad de riesgo femenino (>= 55 años)")

    # 3. Clasificación final
    if puntos_riesgo >= 4:
        nivel = "Alto"
        color = "#d9534f"  # Rojo
    elif puntos_riesgo >= 2:
        nivel = "Moderado"
        color = "#f0ad4e"  # Naranja
    else:
        nivel = "Bajo"
        color = "#5cb85c"  # Verde

    return {
        "imc": imc,
        "nivel_riesgo": nivel,
        "color": color,
        "factores": factores if factores else ["Sin factores de riesgo antropométricos detectados"]
    }
