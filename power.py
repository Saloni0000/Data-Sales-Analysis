import os
import streamlit as st

st.title("Power BI Chart in Streamlit")

# Use os.path.join for cross-platform compatibility
image_file = os.path.join("image", "power_page-0001.jpg")

# Debugging: Print current working directory
st.write(f"Current Directory: {os.getcwd()}")
st.write(f"Looking for file at: {image_file}")

# Check if file exists before displaying
if os.path.exists(image_file):
    st.image(image_file, caption="Power BI Report Visualization", use_container_width=True)  # Updated parameter
else:
    st.error(f"Error: File '{image_file}' not found! Check file path and directory.")
