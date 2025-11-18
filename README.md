# 🌾 Crop Recommendation System

This project implements a Machine Learning–based Crop Recommendation System that suggests the most suitable crop to grow based on soil nutrients and environmental conditions.  
It is designed to support sustainable agriculture by helping farmers and researchers make data-driven decisions.

---

## 📘 Overview

The model takes the following parameters as input:

- **Nitrogen (N)**
- **Phosphorus (P)**
- **Potassium (K)**
- **Temperature**
- **Humidity**
- **Soil pH**
- **Rainfall**

Using these inputs, the trained model predicts the **best crop** suitable for the given conditions.

This project includes:
- A **Jupyter Notebook** for data preprocessing, exploratory analysis, feature engineering, and model training.
- A **Streamlit web application** for real-time crop prediction.

---

## 🧠 Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-Learn  
- Matplotlib / Seaborn  
- Streamlit  
- Jupyter Notebook  

---

## 📁 Project Structure
📂 crop-recommendation-system
├── app.py # Streamlit application
├── Crop_recommendation.ipynb # ML training and analysis notebook
└── README.md # Project documentation

---

## ⚙️ How to Run the Project Locally

### 1️⃣ Install Dependencies

pip install numpy pandas scikit-learn joblib streamlit

### 2️⃣ Train the Model

Open the notebook:
Crop_recommendation.ipynb
Run all cells. This will generate the model file:
crop_model.pkl
(Required by `app.py`)

### 3️⃣ Launch the Streamlit App

streamlit run app.py

This will open the application in your browser.

---

## 📊 Model Details

The notebook includes:

- Data preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature scaling  
- Model training using multiple algorithms  
- Model comparison and evaluation  
- Final model selection  
- Saving the model using Joblib  

The system predicts crops such as **rice, maize, chickpea, kidney beans**, and many more based on soil and climate conditions.

---

## 🚀 Future Enhancements

- Deploy the Streamlit app on the cloud  
- Integrate live weather API  
- Add fertilizer recommendations  
- Add crop disease prediction using deep learning  
- Build an advanced interactive dashboard  

---

## 👩‍💻 Author

**Meghana Reddy Kurapati**  
Information Science & Engineering Student  
Aspiring Data Scientist | ML & AI Enthusiast  
📍 Bengaluru, India

[LinkedIn](https://www.linkedin.com/in/meghanareddy-kurapati-aa02432a2/)


---

