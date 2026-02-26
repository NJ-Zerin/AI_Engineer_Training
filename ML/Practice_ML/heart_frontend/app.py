import streamlit as st
import joblib
import pandas as pd

# ========================
# Load Model Artifacts
# ========================

model = joblib.load("logistic_regression_model.pkl")
scaler = joblib.load("heart_scaler.pkl")
expected_columns = joblib.load("logistic_regression_heart.pkl")

st.title("Heart Disease Prediction ❤️")
st.markdown("Provide the following details")

# ========================
# User Inputs
# ========================

age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
cp = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
rest_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Maximum Heart Rate Achieved", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 10.0, 1.0)
st_slope = st.selectbox("Slope of ST Segment", ["Up", "Flat", "Down"])

# ========================
# Prediction
# ========================

if st.button("Predict"):

    raw_input = pd.DataFrame({
        'Age': [age],
        'Sex': [sex],
        'ChestPainType': [cp],
        'RestingBP': [resting_bp],
        'Cholesterol': [cholesterol],
        'FastingBS': [fasting_bs],
        'RestingECG': [rest_ecg],
        'MaxHR': [max_hr],
        'ExerciseAngina': [exercise_angina],
        'Oldpeak': [oldpeak],
        'ST_Slope': [st_slope]
    })

    # Encode
    input_df = pd.get_dummies(raw_input)
    input_df = input_df.reindex(columns=expected_columns, fill_value=0)

    # Scale
    input_scaled = scaler.transform(input_df)

    # Manual threshold
    probability = model.predict_proba(input_scaled)[0][1]
    threshold = 0.35
    prediction = 1 if probability > threshold else 0

    st.write("Risk Probability:", f"{probability:.2%}")

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")