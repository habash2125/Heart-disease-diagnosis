import fastapi
import pickle
import joblib
import json
import numpy as np
from pydantic import BaseModel
from typing import List,Dict

class patient_info(BaseModel):
    age: str
    sex: str
    cp: str
    trestbps: str
    chol: str
    fbs: str
    restecg: str
    thalach: str
    exang: str
    oldpeak: str
    slope: str
    ca: str
    thal: str
    
app = fastapi.FastAPI()

def preproccess_biometrics(bio_json):

    str_mappings = {'True': 1, 'False': 0, 'Yes': 1, 'No': 0 , "0" : 0}

    print(dict(bio_json))
    bio_json = dict(bio_json)
    #bio_json = json.dump({bio_json})
    
    bio_json["sex"] = int(bio_json["sex"])
    bio_json["cp"] = int(bio_json["cp"])
    bio_json["fbs"] = str_mappings[bio_json["fbs"]]
    bio_json["restecg"] = int(bio_json["restecg"][0])
    bio_json["exang"] = str_mappings[bio_json["exang"]]
    bio_json["slope"] = int(bio_json["slope"][0])
    bio_json["thal"] = int(bio_json["thal"][0])

    bio_json.pop("fbs")
    bio_vector = [int(bio_json[x]) for x in bio_json.keys()]
    print("&&&&& ",bio_vector)
    return bio_vector



@app.post("/prediction")
def prediction(bio_json: patient_info):
    assets_path = "/home/habash/Desktop/grad/models_and_assests/"

    bio_vector = preproccess_biometrics(bio_json)
    bio_vector =np.array(bio_vector)
    print("&&&&& ",bio_vector)
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
