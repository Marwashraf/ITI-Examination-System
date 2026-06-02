import pyodbc
import pandas as pd
import streamlit as st

username = "omarauth"
password = "1234567"
server = "OMAR-GNEEDY\MSSQLSERVER01"
database = "sales" 

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

def student_page():
    st.header("This is student")
    with st.form(key="Login"):
        email = st.text_input("Email")
        password = st.text_input("password") #remember to encrypt password
        st.form_submit_button("Login")
    
def inst_page():
    st.header("This is instructor")
    with st.form(key="Login"):
        email = st.text_input("Email")
        password = st.text_input("password") #remember to encrypt password
        st.form_submit_button("Login")
    query = "SELECT * FROM dbo.ProductDim;"
    df = pd.read_sql(query, cnxn)
    st.dataframe(df)
    
def main_page():
    with st.container():
        st.header("Welcome to ITI")
        st.divider()
        st.subheader("Please choose how you wanna log in!!")
  
    st.divider()
    with st.container():
        col1, col2, col3, col4, col5, col6 = st.columns(6)

        with col3:
            btn1 = st.button("Student")

        with col4:
            btn2 = st.button("Instructor")
            
    if btn1:
        st.session_state.runpage = student_page
        st.session_state.runpage()
        st.experimental_rerun()

    if btn2:
        st.session_state.runpage = inst_page
        st.session_state.runpage()
        st.experimental_rerun()
                              
if 'runpage' not in st.session_state:
    st.session_state.runpage = main_page
st.session_state.runpage()
