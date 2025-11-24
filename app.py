import streamlit as st
import dt, rf, log, svm, knn

st.set_page_config(
    page_title="Apple Quality Prediction",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better aesthetics
st.markdown("""
    <style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background-color: #000000;
    }
    
    h1 {
        color: #e63946;
        text-align: center;
        font-weight: 700;
        margin-bottom: 30px;
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 60px;
        font-weight: 600;
        background-color: #ffffff;
        border: 2px solid #e63946;
        color: #e63946;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #e63946;
        color: white;
        border-color: #e63946;
        transform: scale(1.02);
    }
    
    .stSuccess {
        background-color: #d4edda;
        color: #155724;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🍎 Apple Quality Classification")
st.markdown("<h3 style='text-align: center; color: #457b9d;'>Select a Machine Learning Model</h3>", unsafe_allow_html=True)
st.write("") # Spacer

# Create columns for the buttons with better spacing
col1, col2, col3, col4, col5 = st.columns(5, gap="small")

# Initialize session state for page navigation if not exists
if "page" not in st.session_state:
    st.session_state.page = "dt"

# Button logic with Icons
if col1.button("🌳 Decision Tree"):
    st.session_state.page = "dt"
if col2.button("🌲 Random Forest"):
    st.session_state.page = "rf"
if col3.button("📈 Logistic Reg"):
    st.session_state.page = "log"
if col4.button("⚡ SVM"):
    st.session_state.page = "svm"
if col5.button("📍 KNN"):
    st.session_state.page = "knn"

st.markdown("---")

# Container for the model content
with st.container():
    if st.session_state.page == "dt":
        dt.app()
    elif st.session_state.page == "rf":
        rf.app()
    elif st.session_state.page == "log":
        log.app()
    elif st.session_state.page == "svm":
        svm.app()
    elif st.session_state.page == "knn":
        knn.app()
