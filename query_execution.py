import streamlit as st
import pandas as pd
import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bus_route_allocation_system'
)

cur = db.cursor()

def excecute_query():
    st.title("SQL Query Execution")

    col1,col2=st.columns(2)

    with col1:
        with st.form(key='query_form'):
            raw_code=st.text_area("Sql code here")
            submit_code=st.form_submit_button("Excecute code")


    with col2:
        if submit_code:
            st.info("Query Submitted")
            st.code(raw_code)

            cur.execute(raw_code)
            query_result=cur.fetchall()

            with st.expander("Output"):
                st.write(query_result)
                
            with st.expander("Table"):
                query_df=pd.DataFrame(query_result)
                st.dataframe(query_df)
