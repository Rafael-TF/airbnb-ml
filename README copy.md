# 🏠 Predicción de Precios y Clasificación de Alojamientos en Airbnb NYC 2019

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/a8/Airbnb_Logo_B%C3%A9lo.svg" alt="Airbnb Logo" width="150" style="border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);"/>
</div>

📌 **Proyecto de Machine Learning** para predecir el **precio estimado** de un alojamiento y clasificar su **tipo de habitación** en **Airbnb NYC 2019** utilizando modelos de **Regresión y Clasificación**.  

🚀 **Incluye una aplicación interactiva con Streamlit** para realizar predicciones de forma sencilla.  

---

## 🎯 **Objetivo del Proyecto**

✔️ **Predecir el precio** de un alojamiento basado en sus características.  
✔️ **Clasificar el tipo de habitación** en **Entire home/apt, Private room o Shared room**.  
✔️ **Desplegar una App Interactiva** con **Streamlit** para que los usuarios puedan probar los modelos.  

Este análisis es útil para anfitriones y usuarios que deseen conocer tendencias de precios en Nueva York.  

---

## 📊 **Modelos Utilizados**

<div align="center">

| **Modelo** | **Tarea** | **Técnica Usada** |
|------------|----------|------------------|
| **Gradient Boosting Regressor** | Predicción de Precio | Regresión |
| **Random Forest Classifier** | Clasificación de Tipo de Habitación | Clasificación |

</div>

Ambos modelos fueron **optimizados con `RandomizedSearchCV`** y evaluados con **validación cruzada (5-Fold)** para garantizar su generalización.  

---

## 📈 **Resultados del Modelado**  

<div align="center">

| **Métrica** | **Regresión (Precio)** | **Clasificación (Tipo de Habitación)** |
|------------|----------------|------------------------|
| **R² (Test)**  | 0.9978 | - |
| **MAE** | 0.0131 | - |
| **RMSE** | 0.0273 | - |
| **MAPE** | 2.66% | - |
| **Accuracy** | - | 84.36% |
| **Precision** | - | 84.18% |
| **Recall** | - | 84.36% |
| **F1-Score** | - | 84.25% |
| **AUC** | - | 92.16% |

</div>

---

## ⚙️ **Tecnologías Utilizadas**

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8-blue.svg)  
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)  
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)

</div>

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

## 🌐 Contacto

<div align="center">

📧 **Correo Electrónico:** [<rafa_trafeg@hotmail.com>](mailto:rafa_trafeg@hotmail.com)  
🌍 **Portfolio:** [rafaeltravado.netlify.app](https://rafaeltravado.netlify.app/)  
🔗 **LinkedIn:** [linkedin.rafael-travado](https://www.linkedin.com/in/rafael-travado-4a1b6437/)  

</div>

---

<div align="center" style="margin-top: 30px;">
  <p style="font-size: 16px; color: #555;">📢 **Si te ha gustado el proyecto, dale una ⭐ en GitHub! 🚀**</p>
</div>

📊 **Data Science & Machine Learning en Acción** 🚀
