import streamlit as st
import pandas as pd
import joblib


crop_model = joblib.load("crop_model.pkl")


st.title("🌾 Crop Recommendation System")
st.write(
    "Provide soil nutrient values and climate conditions to get a suitable crop recommendation."
)


nitrogen = st.number_input("Nitrogen (N)", min_value=0.0)
phosphorus = st.number_input("Phosphorus (P)", min_value=0.0)
potassium = st.number_input("Potassium (K)", min_value=0.0)

temperature = st.number_input("Temperature (°C)", min_value=0.0)
humidity = st.number_input("Humidity (%)", min_value=0.0)
soil_ph = st.number_input("Soil pH", min_value=0.0)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0)


if st.button("Recommend Crop"):

   
    nitrogen_phosphorus_ratio = nitrogen / (phosphorus + 1)
    potassium_nitrogen_ratio = potassium / (nitrogen + 1)

   
    climate_index = (temperature + humidity) / 2


    input_data = pd.DataFrame(
        [[
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            soil_ph,
            rainfall,
            nitrogen_phosphorus_ratio,
            potassium_nitrogen_ratio,
            climate_index
        ]],
        columns=[
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall",
            "N_P_ratio",
            "K_N_ratio",
            "climate_index"
        ]
    )
    predicted_crop = crop_model.predict(input_data)
    st.success(f"🌱 Recommended Crop: **{predicted_crop[0]}**")
