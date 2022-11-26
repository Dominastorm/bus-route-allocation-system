import streamlit as st
import yaml

def change_password(authenticator, username, config) -> None:
    try:
        if authenticator.reset_password(username, 'Change password'):
            # write to config file
            with open('./config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
            st.sidebar.success('Password changed successfully')

    except Exception as e:
        st.error(e)