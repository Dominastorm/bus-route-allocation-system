import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from PIL import Image

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
        menu = ['Home', 'Edit Rotue', ]
        choice = st.sidebar.selectbox('',menu)
        st.sidebar._html('<br>')
        # Logout
        authenticator.logout('Logout', 'sidebar')
    
        # MAIN
        if choice == 'Home':
            home(name)

        # Allow user to change password
        try:
            if authenticator.reset_password(username, 'Reset password', 'sidebar'):
                # write to config file
                with open('./config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
                st.sidebar.success('Password changed successfully')

        except Exception as e:
            st.error(e)

        
    # Incorrect username or password
    elif authentication_status == False:
        st.error('Username/password is incorrect')

    # No input provided
    elif authentication_status == None:
        st.warning('Please enter your username and password')

if __name__ == '__main__':
    main()