# 🏠 Predicción de Precios y Clasificación de Alojamientos en Airbnb NYC 2019

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/a8/Airbnb_Logo_B%C3%A9lo.svg" width="150" />
</p>

[![Python](https://img.shields.io/badge/Python-3.8-blue.svg)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)  
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)](https://scikit-learn.org/stable/)  

📌 **Proyecto de Machine Learning** para predecir el **precio estimado** de un alojamiento y clasificar su **tipo de habitación** en **Airbnb NYC 2019** utilizando modelos de **Regresión y Clasificación**.  

🚀 **Incluye una aplicación interactiva con Streamlit** para realizar predicciones de forma sencilla.  

---

## 🎯 **Objetivo del Proyecto**

El propósito principal es analizar datos de **Airbnb NYC 2019** y construir modelos de Machine Learning para:  

✔️ **Predecir el precio** de un alojamiento basado en sus características.  
✔️ **Clasificar el tipo de habitación** en **Entire home/apt, Private room o Shared room**.  
✔️ **Desplegar una App Interactiva** con **Streamlit** para que los usuarios puedan probar los modelos.  

Este análisis es útil para anfitriones y usuarios que deseen conocer tendencias de precios en Nueva York.  

---

## 📊 **Modelos Utilizados**

Se han desarrollado dos modelos principales:

- **Regresión (Predicción de Precio)** → `Gradient Boosting Regressor`  
- **Clasificación (Tipo de Habitación)** → `Random Forest Classifier`  

Ambos modelos fueron **optimizados con `RandomizedSearchCV`** y evaluados con **validación cruzada (5-Fold)** para garantizar su generalización.  

---

## 📈 **Resultados del Modelado**  

### 🔵 **Modelo de Regresión (Predicción de Precio)**

| **Métrica** | **Valor** |
|------------|----------|
| **R² (Test)**  | 0.9978   |
| **MAE**        | 0.0131   |
| **RMSE**       | 0.0273   |
| **MAPE**       | 2.66%    |

📌 **Interpretación:**  
- 🔹 **R² de 0.9978**, lo que indica una predicción altamente precisa del precio.  
- 🔹 **MAE = 0.0131**, margen de error muy bajo.  
- 🔹 **MAPE del 2.66%**, diferencia mínima entre precios reales y predichos.  

### 🔴 **Modelo de Clasificación (Tipo de Habitación)**

| **Métrica**  | **Valor**  |
|-------------|-----------|
| **Accuracy**  | 84.36%   |
| **Precision** | 84.18%   |
| **Recall**    | 84.36%   |
| **F1-Score**  | 84.25%   |
| **AUC**       | 92.16%   |

📌 **Interpretación:**  
- 🔹 **Accuracy del 84.36%**, indica alta capacidad de clasificación.  
- 🔹 **AUC de 92.16%**, buen desempeño en la diferenciación de clases.  
- 🔹 **F1-Score de 84.25%**, balance óptimo entre precisión y recall.  

---

## ⚙️ **Tecnologías Utilizadas**

📌 **Lenguaje y Librerías:**

- 🐍 **Python 3.8**
- 📊 **Pandas & NumPy**
- 🤖 **Scikit-Learn**
- 🎨 **Matplotlib & Seaborn**
- 🌐 **Streamlit**
- 🔗 **Joblib**
- ⚖️ **Imbalanced-Learn (SMOTE)**

---

## 🛠 **Instalación y Ejecución**

### 📥 **1️⃣ Clonar el Repositorio**
```bash
git clone https://github.com/tu_usuario/airbnb-ml.git
cd airbnb-ml
```

### 📦 **2️⃣ Instalar las Dependencias**
```bash
python -m venv venv
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate  # (Windows)
pip install -r requirements.txt
pip install streamlit
```

### 🔄 **3️⃣ Generar los Modelos**
```bash
jupyter notebook notebooks/airbnb_regression.ipynb
jupyter notebook notebooks/airbnb_classification.ipynb
```

### 🚀 **4️⃣ Ejecutar la Aplicación**
```bash
streamlit run app.py
```
💡 Esto abrirá la aplicación en tu navegador en [http://localhost:8501/](http://localhost:8501/).  

---

## 👨‍💻 **Sobre Mí**

📌 **Rafael Travado** - Desarrollador Web Full Stack y entusiasta de Machine Learning.  

📫 **Contacto:**  
- 📧 [rafa_trafeg@hotmail.com](mailto:rafa_trafeg@hotmail.com)  
- 🌍 [Portfolio](https://rafaeltravado.netlify.app/)  
- 🔗 [LinkedIn](https://www.linkedin.com/in/rafael-travado-4a1b6437/)  

📢 **Si te ha gustado el proyecto, dale una ⭐ en GitHub! 🚀**  

📊 **Data Science & Machine Learning en Acción** 🚀
