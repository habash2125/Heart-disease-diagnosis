import fastapi
import pickle
import joblib
import numpy as np
from pydantic import BaseModel
from helpers_func import *
import sqlite3
import os 

class patient_info(BaseModel):
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
    
    
class patient_info_with_pred(BaseModel):
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
    prediction : float

app = fastapi.FastAPI()

@app.post("/prediction")
def prediction(bio_json: patient_info):

    current_path = os.getcwd()
    assets_path = current_path + "/models_and_assests/"


    bio_vector = preproccess_biometrics(bio_json)
    bio_vector =np.array(bio_vector)
    model = joblib.load(assets_path + 'model10.pb')

    with open(assets_path + 'scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

    with open(assets_path + 'pca_10.pkl', 'rb') as pca_file:
        pca = pickle.load(pca_file)

    bio_vector = bio_vector.reshape(1, -1)
    scaled_vec = scaler.transform(bio_vector)
    pcaed_vec = pca.transform(scaled_vec)
    output = np.round(model.predict(pcaed_vec))

    return {"output": output[0][0].tolist()}




@app.post("/add_patient_data")
def add_data(bio_json: patient_info_with_pred):
    
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    database_path = parent_path + '/clevland_replica.db'

    bio_vector = preproccess_biometrics(bio_json, remove_fbs=False)

    con = sqlite3.connect(database_path)
    cur = con.cursor()
    # Generate placeholders for the values in the SQL query
    placeholders = ','.join(['?' for _ in bio_vector])
    # Execute the SQL query with parameterized values
    cur.execute(f"INSERT INTO extended_cleveland VALUES ({placeholders})", bio_vector)

    con.commit()
    
    cur.close()
    con.close()
    return "Done"

