import streamlit as st
import pandas as pd

def upload_csv():

    import pandas as pd
import streamlit as st

def upload_csv():
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    return None
