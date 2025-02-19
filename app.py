import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

# Definir la carpeta donde están los modelos
models_dir = "models"

# Cargar los modelos entrenados
gb_model = joblib.load(os.path.join(models_dir, "gradient_boosting_model.pkl"))  # Modelo de regresión
rf_model = joblib.load(os.path.join(models_dir, "random_forest_classifier.pkl"))  # Modelo de clasificación

# Cargar el preprocesador y el encoder
preprocessor = joblib.load(os.path.join(models_dir, "preprocessor.pkl"))  # Preprocesador de datos numéricos
encoder = joblib.load(os.path.join(models_dir, "encoder.pkl"))  # OneHotEncoder para variables categóricas

# Verificar que el encoder se haya cargado correctamente
if not hasattr(encoder, "transform"):
    st.error("Error al cargar encoder.pkl. Asegúrate de que fue guardado correctamente como un OneHotEncoder.")
    st.stop()

# Título de la Aplicación
st.title("🏠 Predicción de Precios y Tipo de Habitación en Airbnb NYC")

st.markdown("""
### 🔍 Introducción
Esta aplicación permite predecir el **precio estimado** de un alojamiento en Airbnb NYC y clasificar el **tipo de habitación** en función de sus características.
""")

# Definir opciones de "Neighbourhood Group" y "Room Type"
neighbourhood_groups = ["Brooklyn", "Manhattan", "Queens", "Bronx", "Staten Island"]
room_types = ["Entire home/apt", "Private room", "Shared room"]

# Sidebar - Entrada de datos
st.sidebar.header("📌 Parámetros del Alojamiento")
neighbourhood_group = st.sidebar.selectbox("📍 Neighbourhood Group", neighbourhood_groups)
room_type = st.sidebar.selectbox("🛏 Room Type", room_types)
minimum_nights = st.sidebar.slider("📆 Minimum Nights", 1, 365, 3)
number_of_reviews = st.sidebar.slider("💬 Number of Reviews", 0, 500, 10)
reviews_per_month = st.sidebar.slider("⭐ Reviews per Month", 0.0, 10.0, 2.0)
calculated_host_listings_count = st.sidebar.slider("🏠 Host Listings Count", 1, 20, 1)
availability_365 = st.sidebar.slider("📅 Availability (days/year)", 0, 365, 200)
host_ratio = st.sidebar.slider("🤵 Host Ratio", 0.0001, 1.0, 0.05)
review_score = st.sidebar.slider("⭐ Review Score", 0, 100, 50)
neighbourhood_cluster = st.sidebar.slider("📊 Neighbourhood Cluster", 0, 10, 1)

# Crear un DataFrame con los datos ingresados
input_data = pd.DataFrame({
    "neighbourhood_group": [neighbourhood_group],
    "room_type": [room_type],
    "minimum_nights": [minimum_nights],
    "number_of_reviews": [number_of_reviews],
    "reviews_per_month": [reviews_per_month],
    "calculated_host_listings_count": [calculated_host_listings_count],
    "availability_365": [availability_365],
    "host_ratio": [host_ratio],
    "review_score": [review_score],
    "neighbourhood_cluster": [neighbourhood_cluster]
})

# Botón para predecir
if st.sidebar.button("✨ Predecir"):

    ### 🔹 PREPROCESAMIENTO DE VARIABLES CATEGÓRICAS
    input_data_encoded = encoder.transform(input_data[["neighbourhood_group", "room_type"]])
    input_data_encoded_df = pd.DataFrame(
        input_data_encoded, 
        columns=encoder.get_feature_names_out(), 
        index=input_data.index
    )

    ### 🔹 PREPROCESAMIENTO PARA REGRESIÓN (Predicción de Precio)
    # Excluir 'room_type' ya que no se usó en la regresión
    input_data_reg = input_data.drop(columns=["room_type"]).reset_index(drop=True)
    input_data_reg = pd.concat([input_data_reg, input_data_encoded_df], axis=1)

    # Asegurar que las columnas coincidan con el entrenamiento
    for col in preprocessor.feature_names_in_:
        if col not in input_data_reg.columns:
            input_data_reg[col] = 0  # Rellenar con 0 si falta alguna columna

    # Transformar los datos con el preprocesador
    input_data_reg = preprocessor.transform(input_data_reg)

    ### 🔹 PREPROCESAMIENTO PARA CLASIFICACIÓN (Tipo de Habitación)
    # Excluir 'price' ya que no se usó en la clasificación
    input_data_class = input_data.drop(columns=["host_ratio", "review_score"]).reset_index(drop=True)
    input_data_class = pd.concat([input_data_class, input_data_encoded_df], axis=1)

    # Asegurar que las columnas coincidan con el entrenamiento
    for col in preprocessor.feature_names_in_:
        if col not in input_data_class.columns:
            input_data_class[col] = 0  # Rellenar con 0 si falta alguna columna

    # Transformar los datos con el preprocesador
    input_data_class = preprocessor.transform(input_data_class)

    ### 🔹 PREDICCIONES
    # Predicción de precio con el modelo de regresión
    price_log_pred = gb_model.predict(input_data_reg)
    price_pred = np.expm1(price_log_pred)  # Transformar de vuelta a escala original

    # Predicción de tipo de habitación con el modelo de clasificación
    room_pred = rf_model.predict(input_data_class)[0]
    room_proba = rf_model.predict_proba(input_data_class)

    ### 🔹 MOSTRAR RESULTADOS
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