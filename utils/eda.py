import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(df):
    #st.write("### 📈 EDA Plots")

    #if df.select_dtypes(include=["number"]).shape[1] == 2:
       # fig, ax = plt.subplots()
       # sns.scatterplot(data=df, x=df.columns[0], y=df.columns[1], ax=ax)
       # st.pyplot(fig)
   # else:
      # st.warning("Both columns must be numeric for EDA plots.")

    
    if st.checkbox("Show Column Types and Null Values"):
        st.subheader("🧾 Data Info")
        info_df = pd.DataFrame({
            "Data Type": df.dtypes,
            "Nulls": df.isnull().sum(),
            "Unique": df.nunique()
        })
        st.dataframe(info_df)

    # Summary statistics
    if st.checkbox("Show Summary Statistics"):
        st.subheader("📈 Summary Statistics")
        st.dataframe(df.describe().T)

    # Null value heatmap
    if st.checkbox("Visualize Missing Values"):
        st.subheader("🧩 Missing Values Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
        st.pyplot(fig)

    # Correlation heatmap
    if st.checkbox("Correlation Heatmap"):
        st.subheader("🔗 Correlation Matrix")
        numeric_df = df.select_dtypes(include='number')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
        st.pyplot(fig)

    # Distribution plots
    if st.checkbox("Visualize Distributions"):
        st.subheader("🎯 Feature Distributions")
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        selected_cols = st.multiselect("Select numeric columns", numeric_cols)

        for col in selected_cols:
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            ax.set_title(f"Distribution of {col}")
            st.pyplot(fig)