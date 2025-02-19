# 🏠 Predicción de Precios y Clasificación de Alojamientos en Airbnb NYC 2019

[![Python](https://img.shields.io/badge/Python-3.8-blue.svg)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)  
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)](https://scikit-learn.org/stable/)  

📌 **Proyecto de Machine Learning** para predecir el **precio estimado** de un alojamiento y clasificar su **tipo de habitación** en **Airbnb NYC 2019** utilizando modelos de **Regresión y Clasificación**.  

🚀 **Incluye una aplicación interactiva con Streamlit** para realizar predicciones de forma sencilla.  

---

## 🎯 **Objetivo del Proyecto**
El propósito principal es analizar datos de **Airbnb NYC 2019** y construir modelos de Machine Learning para:  

✅ **Predecir el precio** de un alojamiento basado en sus características.  
✅ **Clasificar el tipo de habitación** en **Entire home/apt, Private room o Shared room**.  
✅ **Desplegar una App Interactiva** con **Streamlit** para que los usuarios puedan probar los modelos.  

Este análisis es útil para anfitriones y usuarios que deseen conocer tendencias de precios en Nueva York.  

---

## 📊 **Modelos Utilizados**
Se han desarrollado dos modelos principales:  

🔹 **Regresión (Predicción de Precio) → `Gradient Boosting Regressor`**  
🔹 **Clasificación (Tipo de Habitación) → `Random Forest Classifier`**  

Ambos modelos fueron **optimizados con `RandomizedSearchCV`** y evaluados con **validación cruzada (5-Fold)** para garantizar su generalización.  

## 📈 **Resultados del Modelado**  

### 🔵 **Modelo de Regresión (Predicción de Precio)**
| **Métrica** | **Valor** |
|------------|----------|
| **R² (Test)**  | 0.9978   |
| **MAE**        | 0.0131   |
| **RMSE**       | 0.0273   |
| **MAPE**       | 2.66%    |

📌 **Interpretación:**  
- El modelo **Gradient Boosting** logra un **R² de 0.9978**, lo que indica una predicción altamente precisa del precio.  
- **Error Absoluto Medio (MAE) = 0.0131** sugiere que las predicciones tienen un margen de error muy bajo.  
- **MAPE del 2.66%** confirma que la diferencia entre los precios reales y predichos es mínima.  

---

### 🔴 **Modelo de Clasificación (Tipo de Habitación)**
| **Métrica**  | **Valor**  |
|-------------|-----------|
| **Accuracy**  | 84.36%   |
| **Precision** | 84.18%   |
| **Recall**    | 84.36%   |
| **F1-Score**  | 84.25%   |
| **AUC**       | 92.16%   |

📌 **Interpretación:**  
- El modelo **Random Forest Classifier** obtiene un **Accuracy del 84.36%**, lo que indica una alta capacidad para clasificar correctamente los tipos de habitación.  
- **AUC de 92.16%** confirma que el modelo diferencia bien entre las clases.  
- **F1-Score de 84.25%** sugiere que el balance entre precisión y recall es óptimo.  

---

## ⚙️ **Tecnologías Utilizadas**
Este proyecto fue desarrollado utilizando las siguientes herramientas:  

🔹 **Python 3.8** - Lenguaje de programación  
🔹 **Pandas & NumPy** - Manipulación y análisis de datos  
🔹 **Scikit-Learn** - Modelado de Machine Learning  
🔹 **Streamlit** - Creación de la aplicación web interactiva  
🔹 **Matplotlib & Seaborn** - Visualización de datos  
🔹 **Joblib** - Serialización de modelos entrenados  
🔹 **Imbalanced-Learn (SMOTE)** - Balanceo de clases  

---

## 🛠 **Instalación y Ejecución**
### 📥 **1️⃣ Clonar el Repositorio**
```bash
git clone https://github.com/tu_usuario/airbnb-ml.git
cd airbnb-ml
```

### 📦 **2️⃣ Instalar las Dependencias**
Se recomienda crear un entorno virtual para aislar las dependencias del proyecto:
```bash
python -m venv venv
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate  # (Windows)
```
Instalar los paquetes requeridos con pip:
```bash
pip install -r requirements.txt
```

### 🎯 **3️⃣ Ejecutar la Aplicación en Streamlit**
Ejecuta el siguiente comando para abrir la aplicación:  
```bash
streamlit run app.py
```
💡 Esto abrirá la aplicación en tu navegador en [http://localhost:8501/](http://localhost:8501/).  

---

## 📂 **Estructura del Repositorio**
```
📦 airbnb-nyc-2019-machine-learning  
├── 📂 data                 # Archivos de datos  
│   ├── AB_NYC_2019.csv     # Dataset de Airbnb NYC 2019  
├── 📂 models               # Modelos entrenados guardados con Joblib  
│   ├── gradient_boosting_model.pkl   # Modelo de regresión (predicción de precios)  
│   ├── random_forest_classifier.pkl  # Modelo de clasificación (tipo de habitación)  
├── 📜 Airbnb_NYC_Analysis.ipynb  # Jupyter Notebook con el análisis EDA y modelado  
├── 📜 app.py               # Aplicación Streamlit para predicciones  
├── 📜 requirements.txt     # Dependencias del proyecto  
└── 📜 README.md            # Documentación del proyecto  
```

---

## 🚀 **Ejemplo de Uso**

1️⃣ Selecciona las características del alojamiento en la barra lateral.  
2️⃣ Haz clic en el botón “✨ Predecir” para obtener el precio estimado y el tipo de habitación.  
3️⃣ El resultado se mostrará en pantalla con el precio en dólares y la clasificación de habitación.  

---

## 🔮 **Mejoras Futuras**

Algunas mejoras que se pueden implementar en versiones futuras:
✅ Optimización de modelos con XGBoost o LightGBM.  
✅ Integración de API para datos en tiempo real de Airbnb.  
✅ Visualizaciones más avanzadas con Plotly y Altair.  
✅ Despliegue de la app en la nube con Streamlit Sharing o Heroku.  

---

## 👨‍💻 Sobre Mí

<div align="center">
  <img src="https://github.com/Rafael-TF/Portafolio/raw/main/public/RT.png" alt="Logo Rafael Travado" width="150" style="border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);"/>
</div>

Soy **Rafael Travado**, un apasionado **Desarrollador Web Full Stack** con formación en Derecho. Mi enfoque se centra en crear experiencias digitales efectivas y atractivas que resalten la esencia de cada proyecto. Me encanta enfrentar desafíos tecnológicos y colaborar en iniciativas que marquen la diferencia.

### 📫 ¿Quieres Contactarme?

- **Correo Electrónico:** [rafa_trafeg@hotmail.com](mailto:rafa_trafeg@hotmail.com)
- **Portfolio:** [rafaeltravado.netlify.app](https://rafaeltravado.netlify.app/)
- **LinkedIn:** [linkedin.rafael-travado](https://www.linkedin.com/in/rafael-travado-4a1b6437/)

---

📢 Si te ha gustado el proyecto, dale una ⭐ en GitHub! 🚀  

📊 **Data Science & Machine Learning en Acción** 🚀
