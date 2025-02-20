import streamlit as st

st.title("Power BI Chart in Streamlit")

# Load exported Power BI image file
image_file = "C:\\Users\\sarve\\Downloads\\ilovepdf_pages-to-jpg\\power_page-0001.jpg"  # Replace with your actual file path

# Display Image in Streamlit
st.image(image_file, caption="Power BI Report Visualization", use_column_width=True)
