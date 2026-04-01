import streamlit as st

st.title("InkSight App ✅")

st.write("App is running successfully 🎉")

uploaded_file = st.file_uploader("Upload Image")

if uploaded_file:
    st.image(uploaded_file)

if st.button("Test"):
    st.success("Working perfectly ✅")
