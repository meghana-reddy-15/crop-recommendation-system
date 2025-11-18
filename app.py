import streamlit as st
import pandas as pd
import joblib

model = joblib.load("crop_model.pkl")

st.title("🌾 Crop Recommendation System")
st.write("Enter the values below to get the best crop recommendation.")

N = st.number_input("Nitrogen (N)", 0.0)
P = st.number_input("Phosphorus (P)", 0.0)
K = st.number_input("Potassium (K)", 0.0)
temperature = st.number_input("Temperature", 0.0)
humidity = st.number_input("Humidity", 0.0)
ph = st.number_input("Soil pH", 0.0)
rainfall = st.number_input("Rainfall", 0.0)

if st.button("Recommend Crop"):
    N_P_ratio = N / (P + 1)
    K_N_ratio = K / (N + 1)
    climate_index = (temperature + humidity) / 2

    sample = pd.DataFrame([[
        N, P, K, temperature, humidity, ph, rainfall,
        N_P_ratio, K_N_ratio, climate_index
    ]], columns=[
        'N','P','K','temperature','humidity','ph','rainfall',
        'N_P_ratio','K_N_ratio','climate_index'
    ])

    result = model.predict(sample)
    st.success(f"🌱 Recommended Crop: **{result[0]}**")
