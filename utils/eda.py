import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(df: pd.DataFrame):
    st.write("### ℹ️ Data Info")
    st.write(df.describe())

    col1, col2 = df.columns

    st.write(f"### 📈 Scatter Plot of `{col1}` vs `{col2}`")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=col1, y=col2, ax=ax)
    st.pyplot(fig)

    st.write(f"### 📉 Correlation")
    corr = df.corr()
    st.dataframe(corr)
