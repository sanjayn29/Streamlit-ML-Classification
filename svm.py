import streamlit as st
import numpy as np
import joblib

st.title("🍎 Apple Quality Prediction BY Support Vector Machine Model")

st.write("Enter the apple characteristics below to predict Good or Bad Apple.")

# Load model and scaler using JOBLIB
model = joblib.load("svm_pipeline_model.pkl")
scaler = joblib.load("scaler.pkl")

size = st.number_input("Size")
weight = st.number_input("Weight")
sweetness = st.number_input("Sweetness")
crunchiness = st.number_input("Crunchiness")
juiciness = st.number_input("Juiciness")
ripeness = st.number_input("Ripeness")
acidity = st.number_input("Acidity")

if st.button("Predict"):
    X = np.array([[size, weight, sweetness, crunchiness, juiciness, ripeness, acidity]])
    X_scaled = scaler.transform(X)

    pred = model.predict(X_scaled)[0]

    result = "Good 🍏" if pred == 1 else "Bad 🍎"
    st.success(f"Prediction: **{result}**")
