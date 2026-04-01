import streamlit as st
from streamlit_drawable_canvas import st_canvas
import json

st.title("InkSight: Editable Digital Ink ✍️")

canvas_result = st_canvas(
    stroke_width=5,
    stroke_color="black",
    background_color="white",
    height=300,
    width=300,
    drawing_mode="freedraw",
    key="canvas",
)

# 🟢 SHOW EDITABLE DIGITAL INK DATA
if canvas_result.json_data is not None:
    stroke_data = canvas_result.json_data

    st.subheader("Editable Digital Ink Data (Stroke Format)")
    st.json(stroke_data)

    # Download as file
    st.download_button(
        label="Download Ink Data (JSON)",
        data=json.dumps(stroke_data),
        file_name="ink_data.json",
        mime="application/json"
    )
