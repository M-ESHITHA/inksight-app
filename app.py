import streamlit as st
import numpy as np
from streamlit_drawable_canvas import st_canvas
import cv2

st.title("InkSight: Editable Digital Ink ✍️")

# Drawing canvas (editable)
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0)",
    stroke_width=5,
    stroke_color="black",
    background_color="white",
    height=300,
    width=300,
    drawing_mode="freedraw",
    key="canvas",
)

# Load model
@st.cache_resource
def load_model():
    from tensorflow.keras.models import load_model
    return load_model("model.h5")

model = load_model()

labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # change if needed

if st.button("Predict"):
    if canvas_result.image_data is not None:
        img = canvas_result.image_data

        # Convert to grayscale
        img = cv2.cvtColor(img.astype('uint8'), cv2.COLOR_BGR2GRAY)

        # Resize
        img = cv2.resize(img, (28, 28))

        # Normalize
        img = img / 255.0
        img = img.reshape(1, 28, 28, 1)

        prediction = model.predict(img)
        index = np.argmax(prediction)
        confidence = np.max(prediction) * 100

        st.success(f"Prediction: {labels[index]}")
        st.info(f"Confidence: {confidence:.2f}%")
