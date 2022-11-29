import streamlit as st
import pandas as pd
import mysql.connector
from database import *

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bus_route_allocation_system'
)

cur = db.cursor()


def preset_query():
    operations = ["Insert", "Delete", "Update", "Display", "Search"]
    tables = ["Student", "Bus", "Stop"]

    operations_choice = st.selectbox("Operation", operations)
    tables_choice = st.selectbox("Table", tables)

    if operations_choice == "Insert":
        if tables_choice == "Student":
            insert_student_data_st()
        elif tables_choice == "Bus":
            insert_bus_data_st()
        elif tables_choice == "Stop":
            insert_stop_data_st()

    elif operations_choice == "Update":
        if tables_choice == "Student":
            update_student_data_st()
        elif tables_choice == "Bus":
            update_bus_data_st()
        elif tables_choice == "Stop":
            update_stop_data_st()

    elif operations_choice == "Delete":
        if tables_choice == "Student":
            delete_student_data_st()
        elif tables_choice == "Bus":
            delete_bus_data_st()
        elif tables_choice == "Stop":
            delete_stop_data_st()

    elif operations_choice == "Display":
        if tables_choice == "Student":
            display_student_data_st()
        elif tables_choice == "Bus":
            display_bus_data_st()
        elif tables_choice == "Stop":
            display_stop_data_st()

    elif operations_choice == "Search":
        if tables_choice == "Student":
            search_student_data_st()
        elif tables_choice == "Bus":
            search_bus_data_st()
        elif tables_choice == "Stop":
            search_stop_data_st()


def excecute_query():
    st.title("SQL Query Execution")

    query_mode = ["Preset", "Manual Input"]
    query_choice = st.sidebar.selectbox("Input Method", query_mode)

    if query_choice == "Preset":
        preset_query()
    else:
        col1, col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("Sql code here")
                submit_code = st.form_submit_button("Excecute code")

        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)

                cur.execute(raw_code)
                query_result = cur.fetchall()

                st.write("Results")
                with st.expander("JSON"):
                    st.write(query_result)

                with st.expander("Table"):
                    query_df = pd.DataFrame(query_result)
                    st.dataframe(query_df)
