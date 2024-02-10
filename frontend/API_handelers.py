import streamlit as st
import requests


def handle_submit(biometrics):
    res = requests.post('http://127.0.0.1:8000/prediction', json=biometrics)
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
