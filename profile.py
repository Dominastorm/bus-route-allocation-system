import mysql.connector
import streamlit as st

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bus_route_allocation_system"
)

cursor = db.cursor()

def my_profile(username):
    st.title('My Profile')

    # get the student's details from the database
    cursor.execute(f"SELECT * FROM Student WHERE StudentID = '{username}'")
    result = cursor.fetchall()[0]

    col1, col2 = st.columns(2)

    with col1:
        st.write(f'**User ID:** {result[0]}')
        st.write('**Name:** ', result[4])
        st.write('**Phone:** ', result[5])
        st.write('**Address:** ', result[6])
        
    with col2:
        st.write('**Bus Code:** ', result[2])
        st.write('**Stop Code:** ', result[3])
        st.write('**Transport Fees:** ', result[7])
        st.write('**Admin:** ', ["No", "Yes"][result[8]])