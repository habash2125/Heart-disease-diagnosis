import streamlit as st
import requests
import os

from frontend.interface import create_input_form
from frontend.API_handelers import handle_submit


st.set_page_config(page_title='Patient Info', page_icon='❤️‍🩹')



from dotenv import load_dotenv

def main():
    
    # Load .env file
    load_dotenv()

    # Access environment variables
    value = os.getenv("ENV")
    API_path =os.getenv('api_path')
    
    #st.write(value)
    #print(value)

    biometrics = create_input_form()

    save_state = st.checkbox("save the patient info" ,value = True)
    sub_button = st.button('Submit')

    if sub_button:
        pred = handle_submit(biometrics)
        biometrics['prediction'] = pred
        if save_state : 
            res = requests.post(API_path + 'add_patient_data', json=biometrics)
            if res.status_code == 200:
                print("row added !! ")

if __name__ == '__main__':

    main()

    
