import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from PIL import Image

from database import create_tables
from change_password import change_password
from query_execution import excecute_query
from home import home
from profile import my_profile
from admin_check import check_admin

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
        is_admin = check_admin(username)
        if is_admin:
            menu = ['Home', 'Change Address', 'Change Password', 'Execute Query', 'My Profile', 'Logout']
        else:
            menu = ['Home', 'Change Address', 'Change Password', 'My Profile', 'Logout']
        
        choice = st.sidebar.selectbox('Navigation Menu', menu, label_visibility = 'hidden')
        st.sidebar._html('<br>')

        # create the tables, in case they don't exist
        # create_tables()
        
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
        elif choice == 'Execute Query':
            excecute_query()
        elif choice == 'My Profile':
            my_profile(username)

    # Incorrect username or password
    elif authentication_status == False:
        st.error('Username/password is incorrect')

    # No input provided
    elif authentication_status == None:
        st.warning('Please enter your username and password')

if __name__ == '__main__':
    main()
