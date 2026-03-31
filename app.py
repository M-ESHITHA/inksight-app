import streamlit as st
import numpy as np
from PIL import Image
import cv2

st.title("InkSight: Handwriting Recognition ✍️")

# Load model safely
@st.cache_resource
def load_model():
    try:
        from tensorflow.keras.models import load_model
        model = load_model("model.h5")
        return model
    except:
        return None

model = load_model()

# Upload image
uploaded_file = st.file_uploader("Upload Handwritten Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("L")  # convert to grayscale
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    img = np.array(image)
    img = cv2.resize(img, (28, 28))   # adjust size based on your model
    img = img / 255.0                 # normalize
    img = img.reshape(1, 28, 28, 1)   # reshape for CNN

    if st.button("Predict"):
        if model is not None:
            prediction = model.predict(img)
            result = np.argmax(prediction)

            st.success(f"Predicted Output: {result} ✅")
        else:
            st.error("Model not loaded ❌")
