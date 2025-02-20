import os
import streamlit as st

st.title("Power BI Chart in Streamlit")

image_file = r"image\power_page-0001.jpg"  # Use raw string

# Check if file exists before displaying
if os.path.exists(image_file):
    st.image(image_file, caption="Power BI Report Visualization", use_column_width=True)
else:
    st.error(f"Error: File '{image_file}' not found!")
