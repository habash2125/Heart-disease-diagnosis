import streamlit as st

def create_input_form():
    st.title("Patient Biometrics")
    age = st.number_input("Age (in years)", min_value=1, max_value=100, value=25)
    sex = st.radio("Gender", ["0-Male", "1-Female"])
    cp = st.selectbox("Chest Pain Type", ["1-Typical Angina", "2-Atypical Angina", "3-Non-Anginal Pain", "4-Asymptomatic"])
    trestbps = st.number_input("Resting Blood Pressure (mm/HG)", min_value=80, max_value=200, value=120)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
    fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ['False', 'True'])
    restecg = st.selectbox("Resting ECG Result", ["0-Normal", "1-ST-T Wave Abnormality", "2-Left Ventricular Hypertrophy"])
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=220, value=150)
    exang = st.radio("Exercise Induced Angina", ["No", "Yes"])
    oldpeak = st.number_input("ST-Depression induced by Exercise", min_value=0.0, max_value=7.0, value=0.0)
    slope = st.selectbox("ST Segment Slope during Peak Exercise", ["1-Up Sloping", "2-Flat", "3-Down Sloping"])
    ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia", ["0-None", "3-Normal Blood Flow", "6-Fixed Defect", "7-Reversible Defect"])
    return {
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps,
        "chol": chol, "fbs": fbs, "restecg": restecg, "thalach": thalach,
        "exang": exang, "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal
    }