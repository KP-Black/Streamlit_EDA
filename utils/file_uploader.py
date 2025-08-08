import streamlit as st
import pandas as pd

def upload_csv():

    import pandas as pd
import streamlit as st

#def upload_csv():
 #   uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
  #  if uploaded_file is not None:
   #     df = pd.read_csv(uploaded_file)
    #    return df
   # return None

uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("Data successfully loaded!")

    except Exception as e:
        st.error(f"Error loading file: {e}")
        st.stop()
else:
    st.info("Please upload a file to proceed.")