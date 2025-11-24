import streamlit as st
import numpy as np
import joblib

def app():
    st.markdown("## 📍 K-Nearest Neighbors Model")
    st.info("Enter the apple characteristics below to predict if it's a **Good** or **Bad** Apple.")

    # Load model and scaler using JOBLIB
    model = joblib.load("knn_model.pkl")
    scaler = joblib.load("scaler.pkl")

    col1, col2 = st.columns(2)
    
    with col1:
        size = st.number_input("📏 Size", help="Size of the apple")
        weight = st.number_input("⚖️ Weight", help="Weight of the apple")
        sweetness = st.number_input("🍬 Sweetness", help="Sweetness level")
        crunchiness = st.number_input("🥨 Crunchiness", help="Crunchiness level")
    
    with col2:
        juiciness = st.number_input("🧃 Juiciness", help="Juiciness level")
        ripeness = st.number_input("🕰️ Ripeness", help="Ripeness level")
        acidity = st.number_input("🍋 Acidity", help="Acidity level")

    st.write("")
    if st.button("🔍 Predict Quality", key="predict_knn"):
        X = np.array([[size, weight, sweetness, crunchiness, juiciness, ripeness, acidity]])
        X_scaled = scaler.transform(X)

        pred = model.predict(X_scaled)[0]

        if pred == 1:
            st.success("### Result: **Good Apple 🍏**")
            st.balloons()
        else:
            st.error("### Result: **Bad Apple 🍎**")

if __name__ == "__main__":
    app()
