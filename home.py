import mysql.connector
import streamlit as st

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bus_route_allocation_system"
)

cursor = db.cursor()

def home(username) -> None:
    
    # get the student's details from the database
    cursor.execute(f"SELECT * FROM Student WHERE StudentID = '{username}'")
    student = cursor.fetchall()[0]
    cursor.execute(f"SELECT * FROM Bus WHERE BusCode = {student[2]}")
    bus = cursor.fetchall()[0]
    cursor.execute(f"SELECT * FROM Stop WHERE RouteCode = {bus[1]} AND StopCode = {student[3]}")
    stop = cursor.fetchall()[0]
    
    st.markdown(f'<h2>Welcome, {student[4]}!</h2><br>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    with col1:
        st.write(f'**Bus Code:** {bus[0]}')
        st.write(f'**Bus Number:** {bus[2]}')
        st.write(f'**Driver Name:** {bus[3]}')
        st.write(f'**Driver Phone:** {bus[4]}')
        
    with col2:
        st.write(f'**Stop Name:** {stop[2]}')
        st.write(f'**Stop Address:** {stop[3]}')
        st.write(f'**Pickup Time:** {stop[4]}')
        st.write(f'**Drop Time:** {stop[5]}')
        st.write(f'**Distance from College:** {stop[6]}')
