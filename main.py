import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Examen Diagnóstico - Álgebra Lineal")

st.title("Examen Diagnóstico – Álgebra Lineal - Aplicacion desarrollada por Arq. Eduardo Ramirez, Joanna Rodriguez, Irma Carrillo")
st.write("Nombre del alumno(a):")
student_name = st.text_input("Ingresa tu nombre")

st.markdown("---")

questions = [
    {
        "question": "1. ¿Qué es el álgebra lineal?",
        "options": [
            "Un área de la geometría enfocada en figuras tridimensionales",
            "Una rama de las matemáticas que estudia vectores, matrices y sistemas lineales",
            "Un conjunto de fórmulas aplicadas en cálculo diferencial",
            "Un tema que solo se relaciona con la contabilidad"
        ]
    },
    {
        "question": "2. ¿Cuál de las siguientes opciones define mejor a un vector en álgebra lineal?",
        "options": [
            "Una función que mide la pendiente de una recta",
            "Una figura con forma de flecha que representa magnitud y dirección",
            "Una operación aritmética entre matrices",
            "Una constante sin unidades"
        ]
    },
    {
        "question": "3. ¿Qué indica obtener una fila como 0 = 5 al resolver un sistema de ecuaciones lineales?",
        "options": [
            "El sistema tiene infinitas soluciones",
            "El sistema tiene una única solución",
            "El sistema es inconsistente y no tiene solución",
            "El sistema tiene variables libres"
        ]
    },
    {
        "question": "4. ¿Qué significa obtener una fila completa de ceros en una matriz al resolver un sistema?",
        "options": [
            "Hay una solución única",
            "Hay un error de cálculo",
            "El sistema es inconsistente",
            "Hay variables libres e infinitas soluciones"
        ]
    },
    {
        "question": "5. Un carpintero quiere construir una mesa de 12 metros de largo gastando exactamente 170mxn usando tablas tipo A (30mxn, 2 m) y tipo B (40mxn, 3 m). ¿Cuál es el sistema de ecuaciones que representa este problema?",
        "options": [
            "2x + 3y = 12,    30x + 40y = 170",
            "2x + 3y = 170,   30x + 40y = 12",
            "x + y = 12,      x + y = 170",
            "30x + 40y = 12,  2x + 3y = 170"
        ]
    },
    {
        "question": "6. ¿Cuál de los siguientes enunciados es falso respecto a una matriz?",
        "options": [
            "Una matriz puede representar un sistema de ecuaciones lineales",
            "Las filas de una matriz corresponden a ecuaciones",
            "Las columnas de una matriz representan variables",
            "Una matriz solo puede tener números positivos"
        ]
    },
    {
        "question": "7. ¿Qué propiedad permite intercambiar dos filas en una matriz sin alterar la solución del sistema?",
        "options": [
            "Conmutativa",
            "Distributiva",
            "Operación elemental",
            "Asociativa"
        ]
    },
    {
        "question": "8. ¿Cuál es la forma escalonada de una matriz?",
        "options": [
            "Cuando todas las entradas son cero",
            "Cuando la matriz tiene ceros debajo de la diagonal principal",
            "Cuando todos los números están ordenados alfabéticamente",
            "Cuando los vectores son ortogonales"
        ]
    },
    {
        "question": "9. ¿Qué representa geométricamente la solución de un sistema de ecuaciones lineales con dos incógnitas?",
        "options": [
            "Un punto, una recta o ninguna intersección",
            "Un triángulo",
            "Una parábola",
            "Un círculo"
        ]
    },
    {
        "question": "10. Evalúa si la siguiente igualdad es verdadera o falsa: (2x+3)(x−1)−(x²+x−4) = 7−x",
        "options": [
            "Verdadera para todo valor de x",
            "Falsa para todo valor de x",
            "Verdadera solo si x = 1",
            "No se puede saber sin resolver"
        ]
    }
]

responses = {}

for i, q in enumerate(questions):
    responses[f"Q{i+1}"] = st.radio(q["question"], q["options"], key=f"q{i+1}")

# Guardar respuestas
if st.button("Guardar respuestas"):
    if not student_name.strip():
        st.warning("Por favor, escribe tu nombre antes de enviar.")
    else:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "Nombre": student_name,
            "Fecha": timestamp,
        }
        data.update(responses)

        df = pd.DataFrame([data])
        csv_filename = "respuestas_examen_algebra.csv"

        try:
            existing_df = pd.read_csv(csv_filename)
            df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            pass

        df.to_csv(csv_filename, index=False)
        st.success("Respuestas guardadas correctamente en respuestas_examen_algebra.csv")

