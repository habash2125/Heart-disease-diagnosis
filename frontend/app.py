import streamlit as st
import requests
import os

from interface import create_input_form
from API_handelers import handle_submit

from config import Config

st.set_page_config(page_title='Patient Info', page_icon='❤️‍🩹')



from dotenv import load_dotenv

def main():
    
    # Load .env file
    load_dotenv()

    env = os.getenv("ENV")
    config = Config[env]
    API_path = config['api_path']
    print("ENV : ", env)
    biometrics = create_input_form()

    save_state = st.checkbox("save the patient info" ,value = True)
    submit_button = st.button('Submit')

    if submit_button:
        pred = handle_submit(biometrics)
        biometrics['prediction'] = pred

        if save_state :
            try :
                res = requests.post(API_path + 'add_patient_data', json=biometrics)
                if res.status_code == 200:
                    print("row added !! ")
                else:
                    print("response Erorr")

            except Exception as e:
                print("api connection error: ", e)
                st.write("error inserting row!!")

if __name__ == '__main__':
    main()

    
