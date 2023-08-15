import streamlit as st
import numpy as np
from keras.models import load_model

# Load the trained model
model = load_model('my_trained_model.h5')

st.title("Food Delivery Time Prediction")

# Input fields for user to provide the delivery partner's age, ratings, and distance
age = st.number_input("Age of Delivery Partner", min_value=18, max_value=70, value=30)
ratings = st.number_input("Ratings of Previous Deliveries", min_value=0.0, max_value=5.0, value=4.5, step=0.1)
distance = st.number_input("Total Distance", min_value=1, value=5)

# Predict button
if st.button("Predict"):
    features = np.array([[age, ratings, distance]])
    predicted_time = model.predict(features)
    st.write(f"Predicted Delivery Time in {predicted_time[0][0]:.2f} Minutes")
