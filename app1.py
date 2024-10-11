import streamlit as st
import joblib
import os

# Attempt to load the pre-trained model
try:
    model = joblib.load("student_performance.pkl")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()  # Stop execution if the model fails to load

# Streamlit app title
st.title("Student Performance")

# Check for image file
image_path = "studentimg.png"
if os.path.exists(image_path):
    st.image(image_path, width=600)
else:
    st.error(f"Image file '{image_path}' not found. Please check the path.")

# Inputs from user
study_time = st.number_input("Pleas your study time:", min_value=0, step=1)
attendance = st.number_input("Please enter your Attendance:", min_value=0, step=1)
extracurricular = st.number_input("Please enter your Extracurricular Activities Score:", min_value=0, step=1)

# Prediction
if st.button("Predict Student Performance"):
    try:
        result = model.predict([[study_time, attendance, extracurricular]])
        st.success(f"Predicted Student Performance: {result[0]:,.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
