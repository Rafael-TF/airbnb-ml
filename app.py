import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Cargar los modelos entrenados
gb_model = joblib.load("gradient_boosting_model.pkl")  # Modelo de regresión
rf_model = joblib.load("random_forest_classifier.pkl")  # Modelo de clasificación

# Título de la Aplicación
st.title("🏠 Predicción de Precios y Tipo de Habitación en Airbnb NYC")

st.markdown("""
### 🔍 Introducción
Esta aplicación permite predecir el **precio estimado** de un alojamiento en Airbnb NYC y clasificar el **tipo de habitación** 
en función de sus características.
""")

# Definir opciones de "Neighbourhood Group"
neighbourhood_groups = ["Brooklyn", "Manhattan", "Queens", "Bronx", "Staten Island"]

# Sidebar - Entrada de datos
st.sidebar.header("📌 Parámetros del Alojamiento")
neighbourhood_group = st.sidebar.selectbox("📍 Neighbourhood Group", neighbourhood_groups)
minimum_nights = st.sidebar.slider("📆 Minimum Nights", 1, 365, 3)
number_of_reviews = st.sidebar.slider("💬 Number of Reviews", 0, 500, 10)
reviews_per_month = st.sidebar.slider("⭐ Reviews per Month", 0.0, 10.0, 2.0)
calculated_host_listings_count = st.sidebar.slider("🏠 Host Listings Count", 1, 20, 1)
availability_365 = st.sidebar.slider("📅 Availability (days/year)", 0, 365, 200)

# Crear un DataFrame con los datos ingresados
input_data = pd.DataFrame({
    "neighbourhood_group": [neighbourhood_group],
    "minimum_nights": [minimum_nights],
    "number_of_reviews": [number_of_reviews],
    "reviews_per_month": [reviews_per_month],
    "calculated_host_listings_count": [calculated_host_listings_count],
    "availability_365": [availability_365]
})

# Botón para predecir
if st.sidebar.button("✨ Predecir"):

    # Convertir la variable categórica a numérica
    input_data["neighbourhood_group"] = input_data["neighbourhood_group"].map({
        "Brooklyn": 0, "Manhattan": 1, "Queens": 2, "Bronx": 3, "Staten Island": 4
    })

    # Predicción de precio con el modelo de regresión
    price_log_pred = gb_model.predict(input_data)
    price_pred = np.expm1(price_log_pred)  # Transformar de vuelta a escala original

    # Predicción de tipo de habitación con el modelo de clasificación
    room_pred = rf_model.predict(input_data)[0]
    room_proba = rf_model.predict_proba(input_data)

    # Mostrar resultados
    st.subheader("📌 Resultados de la Predicción")
    st.success(f"💰 **Precio Estimado:** ${price_pred[0]:,.2f}")
    
    st.info(f"🛏 **Tipo de Habitación Predicho:** {room_pred}")

    # Mostrar probabilidades de predicción para cada tipo de habitación
    st.subheader("🔍 Probabilidad de cada Tipo de Habitación")
    room_labels = rf_model.classes_
    room_probs = {label: round(proba * 100, 2) for label, proba in zip(room_labels, room_proba[0])}
    st.json(room_probs)

st.sidebar.markdown("---")
st.sidebar.markdown("📊 **Desarrollado por Rafael Travado**")