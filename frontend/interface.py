import streamlit as st
from typing import TypedDict

# Define constants for choices
GENDER_CHOICES = ["0-Male", "1-Female"]
CHEST_PAIN_CHOICES = [
    "1-Typical Angina", "2-Atypical Angina",
    "3-Non-Anginal Pain", "4-Asymptomatic"
]
FBS_CHOICES = ['False', 'True']
REST_ECG_CHOICES = [
    "0-Normal", "1-ST-T Wave Abnormality",
    "2-Left Ventricular Hypertrophy"
]
EXANG_CHOICES = ["No", "Yes"]
SLOPE_CHOICES = ["1-Up Sloping", "2-Flat", "3-Down Sloping"]
THAL_CHOICES = [
    "0-None", "3-Normal Blood Flow",
    "6-Fixed Defect", "7-Reversible Defect"
]
CA_CHOICES = [0, 1, 2, 3]


class PatientData(TypedDict):
    age: int
    sex: str
    cp: str
    trestbps: int
    chol: int
    fbs: str
    restecg: str
    thalach: int
    exang: str
    oldpeak: float
    slope: str
    ca: int
    thal: str


def create_input_form() -> PatientData:
    st.title("Patient Biometrics")

    age = st.number_input("Age (in years)", min_value=1, max_value=100, value=25)
    sex = st.radio("Gender", GENDER_CHOICES)
    cp = st.selectbox("Chest Pain Type", CHEST_PAIN_CHOICES)
    trestbps = st.number_input("Resting Blood Pressure (mm/HG)", min_value=80, max_value=200, value=120)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
    fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", FBS_CHOICES)
    restecg = st.selectbox("Resting ECG Result", REST_ECG_CHOICES)
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=220, value=150)
    exang = st.radio("Exercise Induced Angina", EXANG_CHOICES)
    oldpeak = st.number_input("ST-Depression induced by Exercise", min_value=0.0, max_value=7.0, value=0.0)
    slope = st.selectbox("ST Segment Slope during Peak Exercise", SLOPE_CHOICES)
    ca = st.selectbox("Number of Major Vessels", CA_CHOICES)
    thal = st.selectbox("Thalassemia", THAL_CHOICES)

    return {
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps,
        "chol": chol, "fbs": fbs, "restecg": restecg, "thalach": thalach,
        "exang": exang, "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal
    }

