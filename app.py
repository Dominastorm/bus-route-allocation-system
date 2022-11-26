import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Load the configuration file
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create the authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Authenticate the user
name, authentication_status, username = authenticator.login('Login', 'main')

# If the user is authenticated, display the app
if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.write(f'Welcome, *{name}*!')
    st.title('Some content')
    # Allow user to change password
    try:
        if authenticator.reset_password(username, 'Reset password', 'sidebar'):
            # write to config file
            with open('./config.yaml', 'w') as file:
                yaml.dump(config, file)
            st.sidebar.success('Password changed successfully')
    except Exception as e:
        st.error(e)

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

