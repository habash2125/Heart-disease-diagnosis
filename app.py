import streamlit as st
import requests
from frontend.interface import create_input_form
from frontend.API_handelers import handle_submit
st.set_page_config(page_title='Patient Info', page_icon='❤️‍🩹')




def main():
    biometrics = create_input_form()

    save_state = st.checkbox("save the patient info" ,value = True)
    sub_button = st.button('Submit')

    if sub_button:
        pred = handle_submit(biometrics)
        biometrics['prediction'] = pred
        if save_state : 
            res = requests.post('http://127.0.0.1:8000/add_patient_data', json=biometrics)
            print(res.text)
            if res.status_code == 200:
                print("row added !! ")

if __name__ == '__main__':
    main()

