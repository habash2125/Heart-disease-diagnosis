import streamlit as st
import requests
from frontend.interface import create_input_form
from frontend.API_handelers import handle_submit
st.set_page_config(page_title='Patient Info', page_icon='❤️‍🩹')




def main():
    biometrics = create_input_form()
    sub_button = st.button('Submit')
    if sub_button:
        handle_submit(biometrics)

if __name__ == '__main__':
    main()

