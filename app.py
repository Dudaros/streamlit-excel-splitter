import streamlit as st
import pandas as pd
import io

st.title("Excel Column Splitter")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("📊 **Preview of Uploaded Data:**")
    st.dataframe(df)  # Show the uploaded data

    column_to_split = st.selectbox("Select column to split by", df.columns)

    if st.button("Split File"):
        unique_values = df[column_to_split].unique()
        st.write(f"🔍 **Unique values in '{column_to_split}':** {unique_values}")

        for value in unique_values:
            subset = df[df[column_to_split] == value]  # This filters correctly

            # Debugging: Show first few rows of each subset
            st.write(f"📂 **Splitting for '{value}':**")
            st.dataframe(subset)

            # Convert to Excel in memory
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                subset.to_excel(writer, index=False)
            output.seek(0)

            # Provide a download button
            st.download_button(
                label=f"📥 Download {value}.xlsx",
                data=output,
                file_name=f"{value}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )

        st.success("✅ Files are ready for download!")
