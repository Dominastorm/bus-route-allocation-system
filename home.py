import streamlit as st

def home(name) -> None:
    st.markdown(f'<h2>Welcome, {name}!</h2>', unsafe_allow_html=True)
