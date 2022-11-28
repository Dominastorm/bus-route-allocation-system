import mysql.connector
import streamlit as st

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bus_route_allocation_system"
)

cursor = db.cursor()

def check_admin(username):
    cursor.execute(f"SELECT isAdmin FROM Student WHERE StudentID = '{username}'")
    result = cursor.fetchone()
    if result[0] == 1:
        return True
    else:
        return False
        