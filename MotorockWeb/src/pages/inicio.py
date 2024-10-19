import streamlit as st
import requests

st.markdown("""
    <style>
        .st-emotion-cache-yfhhig {
            visibility: hidden;
        }
        .st-emotion-cache-mnu3yk {
            visibility: hidden
        } 
        
    </style>
""", unsafe_allow_html=True)

url = "http://localhost:8081/v1/fileProcess/upload"

uploaded_pdf = st.file_uploader('Upload a file', type="csv")
if st.button("Upload CSV"):
    files = {'file': (uploaded_pdf)}
    response = requests.post(url, files=files)
    st.write(response)