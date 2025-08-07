import streamlit as st
from utils.file_uploader import upload_csv
from utils.eda import perform_eda

st.set_page_config(page_title="Modular EDA App", layout="centered")

st.title("📊 Modular EDA App (Two Columns Only)")

df = upload_csv()

if df is not None:
    st.write("### 📄 Uploaded Data", df.head())

    if df.shape[1] == 2:
        perform_eda(df)
    else:
        st.warning("Please upload a dataset with exactly two columns.")
