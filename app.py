import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from PIL import Image
from change_password import change_password

from home import home

def main() -> None:
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

    # Add a logo to the sidebar
    image = Image.open('assets/images/logo.png')
    st.sidebar.image(image, use_column_width=True)
    st.sidebar.title('Bus Route Allocation System')
    

    # Authenticate the user
    name, authentication_status, username = authenticator.login('Login', 'main')
    
    # If the user is authenticated, display the app
    if authentication_status:
        # SIDEBAR
        menu = ['Home', 'Change Address', 'Change Password', 'Logout']
        choice = st.sidebar.selectbox('',menu)
        st.sidebar._html('<br>')
        
        # MAIN
        if choice == 'Home':
            home(name)
        elif choice == 'Change Address':
            pass
        elif choice == 'Change Password':
            change_password(authenticator, username, config)
        elif choice == 'Logout':
            st.write('Are you sure you want to log out?')
            authenticator.logout('Logout', 'main')
        

    # Incorrect username or password
    elif authentication_status == False:
        st.error('Username/password is incorrect')

    # No input provided
    elif authentication_status == None:
        st.warning('Please enter your username and password')

if __name__ == '__main__':
    main()