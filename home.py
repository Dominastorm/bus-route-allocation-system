import streamlit as st
from change_password import change_password

def home(name) -> None:
    st.markdown(f'<h2>Welcome, {name}!</h2>', unsafe_allow_html=True)
    st.write('Route Name: {}')
    
