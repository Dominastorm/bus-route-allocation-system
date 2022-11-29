import streamlit as st
import yaml
import mysql.connector
import streamlit_authenticator as stauth

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bus_route_allocation_system"
)

cursor = db.cursor()


def change_password(authenticator, username, config) -> None:
    try:
        new_password = authenticator.reset_password(
            username, 'Change Password')

        if new_password:
            # write to database
            cursor.execute(
                f"UPDATE Student SET Password = '{new_password}' WHERE StudentID = '{username}'")
            db.commit()
            st.sidebar.success('Password changed successfully!')

    except Exception as e:
        st.error(e)
