from pydantic import BaseModel


class PatientInfo(BaseModel):
    age: float
    sex: str
    cp: str
    trestbps: float
    chol: float
    fbs: str
    restecg: str
    thalach: float
    exang: str
    oldpeak: float
    slope: str
    ca: float
    thal: str


class PatientInfoWithPred(BaseModel):
    age: float
    sex: str
    cp: str
    trestbps: float
    chol: float
    fbs: str
    restecg: str
    thalach: float
    exang: str
    oldpeak: float
    slope: str
    ca: float
    thal: str
    prediction: float
