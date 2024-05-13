import streamlit as st
import requests
import os

from interface import create_input_form
from API_handelers import handle_submit


st.set_page_config(page_title='Patient Info', page_icon='❤️‍🩹')



from dotenv import load_dotenv

def main():
    
    # Load .env file
    load_dotenv()

    API_path = "http://127.0.0.1:8000/"

    biometrics = create_input_form()

    save_state = st.checkbox("save the patient info" ,value = True)
    sub_button = st.button('Submit')

    if sub_button:
        pred = handle_submit(biometrics)
        biometrics['prediction'] = pred
        if save_state :
            st.write(API_path)
            print("######" , API_path , "3333333333333")

            res = requests.post(API_path + 'add_patient_data', json=biometrics)
            if res.status_code == 200:
                print("row added !! ")

if __name__ == '__main__':

    main()

    
