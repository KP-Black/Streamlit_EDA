import streamlit as st
import pandas as pd

def upload_csv():
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            return df
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")
            return None
    return None
