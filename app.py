import streamlit as st
import pandas as pd

st.title("Excel Column Splitter")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    column_to_split = st.selectbox("Select column to split by", df.columns)

    if st.button("Split File"):
        unique_values = df[column_to_split].unique()
        for value in unique_values:
            subset = df[df[column_to_split] == value]
            subset.to_excel(f"{value}.xlsx", index=False)

        st.success("Files have been split! Download them from the output folder.")
