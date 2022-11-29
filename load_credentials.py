import mysql.connector
import streamlit as st
import streamlit_authenticator as stauth

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bus_route_allocation_system"
)

cursor = db.cursor()

def load_credentials():
    cursor.execute("SELECT StudentID, StudentName, Password FROM Student")
    result = cursor.fetchall()
    credentials = {}
    for row in result:
        username = row[0]
        name = row[1]
        password = stauth.Hasher([row[2]]).generate()[0]
        credentials[username] = {'password': password, 'name': name}
    return credentials
    