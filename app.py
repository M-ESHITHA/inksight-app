import streamlit as st

st.title("InkSight: Handwriting to Digital")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file)

if st.button("Predict"):
    st.write("Working ✅")