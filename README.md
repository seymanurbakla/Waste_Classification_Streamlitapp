# Waste Classification Streamlit App

This repository contains a Streamlit application for waste classification using an AI model developed with YOLOv8m-cls. The application can accurately classify waste into 10 categories: **biodegradable, cardboard, glass, gloves, masks, medicines, metal, paper, plastic, syringe, and organic waste**.

---

## Project Overview

The aim of this project is to promote environmental awareness and waste management by leveraging AI technology. The model was trained on a comprehensive dataset with 17,500 images and demonstrates high accuracy in classifying waste into the specified categories.

### Key Features:
- **Real-time Waste Classification**: Upload an image to see its predicted waste category.
- **Interactive Visuals**: The application provides visualizations of predictions and classification performance.
- **User-Friendly Interface**: Built with Streamlit for ease of use.

---

## Model Training Details

The model was trained using **YOLOv8m-cls** in a Google Colab environment. The training parameters and steps are as follows:

1. **Environment Setup**:  
   Mounted Google Drive and set the working directory.  

   ```python
   from google.colab import drive
   drive.mount("/content/drive")
   import os
   colab_dir = "/content/drive/MyDrive/Waste_classification"
   os.chdir(colab_dir)
