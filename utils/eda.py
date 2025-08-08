import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(df):
    st.write("### 📈 EDA Plots")

    if df.select_dtypes(include=["number"]).shape[1] == 2:
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=df.columns[0], y=df.columns[1], ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Both columns must be numeric for EDA plots.")

    
    
    