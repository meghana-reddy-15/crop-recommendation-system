import streamlit as st
import pandas as pd
import joblib


# -------------------- Load Model --------------------
@st.cache_resource
def load_model():
    return joblib.load("crop_model.pkl")


model = load_model()


# -------------------- UI --------------------
st.title("🌾 Crop Recommendation System")
st.write(
    "Enter soil nutrient values and climate conditions. "
    "The system will recommend a suitable crop based on trained ML predictions."
)


# -------------------- Input Section --------------------
st.subheader("Soil Nutrients")
nitrogen = st.number_input("Nitrogen (N)", min_value=0.0)
phosphorus = st.number_input("Phosphorus (P)", min_value=0.0)
potassium = st.number_input("Potassium (K)", min_value=0.0)

st.subheader("Climate Conditions")
temperature = st.number_input("Temperature (°C)", min_value=0.0)
humidity = st.number_input("Humidity (%)", min_value=0.0)
soil_ph = st.number_input("Soil pH", min_value=0.0)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0)


# -------------------- Feature Engineering --------------------
def create_features():
    """
    Create additional derived features from raw inputs
    to help the ML model capture relationships better.
    """
    n_p_ratio = nitrogen / (phosphorus + 1)
    k_n_ratio = potassium / (nitrogen + 1)
    climate_index = (temperature + humidity) / 2

    return pd.DataFrame(
        [[
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            soil_ph,
            rainfall,
            n_p_ratio,
            k_n_ratio,
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


# -------------------- Prediction --------------------
if st.button("Recommend Crop"):

    if nitrogen == 0 and phosphorus == 0 and potassium == 0:
        st.warning("Please enter valid soil nutrient values.")
    else:
        input_df = create_features()
        prediction = model.predict(input_df)

        st.success(
            f"🌱 **Recommended Crop:** {prediction[0]}"
        )

        st.caption(
            "Recommendation is based on soil nutrients, climate conditions, "
            "and engineered features such as nutrient ratios."
        )
