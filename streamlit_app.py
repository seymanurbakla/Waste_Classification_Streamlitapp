#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:27:38 2024

@author: seynoma
"""

import streamlit as st
from PIL import Image
from torchvision import transforms
from ultralytics import YOLO

#import streamlit as st
from PIL import Image
from torchvision import transforms
from ultralytics import YOLO

# Title and description
st.title("Waste Classification Streamlit App")
st.write("""
This app helps classify waste into 10 categories using a YOLOv8 classification model:
- Biodegradable
- Cardboard
- Glass
- Gloves
- Masks
- Medicines
- Metal
- Paper
- Plastic
- Syringe

Upload an image of waste, and the model will classify it to promote recycling and environmental awareness. 🌱
""")

# Load the model
@st.cache_resource
def load_model():
    model = YOLO("best.pt")  # Replace with your model path
    return model

model = load_model()

# Image uploader
uploaded_file = st.file_uploader("Upload a waste image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    img_tensor = preprocess(image).unsqueeze(0)

    # Perform inference
    with st.spinner("Classifying..."):
        results = model.predict(img_tensor)
        class_index = results[0].probs.top1  # Get predicted class index
        confidence = results[0].probs.top1conf  # Get confidence score

    # Define class labels
    class_labels = [
        "Biodegradable", "Cardboard", "Glass", "Gloves", "Masks",
        "Medicines", "Metal", "Paper", "Plastic", "Syringe"
    ]
    predicted_class = class_labels[class_index]

    # Display result
    st.success(f"Prediction: **{predicted_class}**")
    st.write(f"Confidence: **{confidence:.2f}**")

st.write("---")
st.write("Developed using **YOLOv8** and **Streamlit**. Let's promote recycling together! 🚀")
