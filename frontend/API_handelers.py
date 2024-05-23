import streamlit as st
import requests
import os 
from dotenv import load_dotenv
from config import Config
def handle_submit(biometrics):

     # Load .env file
    load_dotenv()

    # Access environment variables
    env = os.getenv("ENV")
    config = Config[env]
    API_path = config["api_path"]
    output = None
    res = requests.post(API_path + 'prediction', json=biometrics)
    if res.status_code == 200:
        response_data = res.json()
        output = response_data.get('output', None)
        if output is not None:
            if output == 1:
                st.write("Have a heart disease")
            else:
                st.write("Do not have a heart disease")
    else:
        st.error(f"Error: {res.status_code}")
    
    return output
