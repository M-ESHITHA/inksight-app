import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("InkSight: Editable Digital Ink ✍️")

# Canvas
canvas_result = st_canvas(
    stroke_width=5,
    stroke_color="black",
    background_color="white",
    height=300,
    width=300,
    drawing_mode="freedraw",
    key="canvas",
)

# SAFE prediction button (no tensorflow)
if st.button("Predict"):
    st.success("Canvas Working ✅ (Model not connected yet)")
