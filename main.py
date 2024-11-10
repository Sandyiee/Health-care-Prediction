import pickle
import streamlit as st
import pandas as pd
from PIL import Image
import base64

# Set up Streamlit app configuration
st.set_page_config(
    page_title="Health Care Predictor",
    page_icon="☠️",
    initial_sidebar_state="expanded",
)

# Convert the main image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# HTML and CSS to display only the main image
main_bg =r"D:/projects/Heart/heart.jpeg"
main_bg_base64 = get_base64_image(main_bg)

html_temp = f"""
<div style="position: relative; text-align: center;">
    <img src="data:image/jpg;base64,{main_bg_base64}" style="width: 100%; height: auto;">
</div>
"""

# Display the HTML with the background image only
st.markdown(html_temp, unsafe_allow_html=True)

# Load the trained model
pickle_in = open('health_care_random_forest.pkl', 'rb') 
classifier = pickle.load(pickle_in)

# Define the prediction function
def prediction(Age, gender, height, weight, bmi, bp_hi, bp_lo, cholesterol, glucose, smoke, alcohol, edema, jaundice, Creatinine, Creatinine_clearance, GFR, Polycythemia, Leukemia):  
    prediction = classifier.predict( 
        [[Age, gender, height, weight, bmi, bp_hi, bp_lo, cholesterol, glucose, smoke, alcohol, edema, jaundice, Creatinine, Creatinine_clearance, GFR, Polycythemia, Leukemia]])
    return prediction

# Layout for user input
col1, col2 = st.columns(2)

with col1:
    Age = st.number_input("1. Enter your age?")
    height = st.number_input("3. Enter your height in cm")
    bmi = st.number_input("5. Enter your Body Mass Index (BMI)")
    bp_lo = st.number_input("7. Enter your lowest BP level")
    glucose = st.number_input("9. Enter your glucose level")
    alcohol = st.number_input("11. Enter your alcohol level")
    jaundice = st.number_input("13. Enter your jaundice level")
    Creatinine_clearance = st.number_input("15. Enter your Creatinine clearance level")
    Polycythemia = st.number_input("17. Enter your Polycythemia level")

with col2:
    gender = st.number_input("2. Enter your gender")
    weight = st.number_input("4. Enter your weight")
    bp_hi = st.number_input("6. Enter your highest BP level")
    cholesterol = st.number_input("8. Enter your cholesterol level")
    smoke = st.number_input("10. Do you smoke?")
    edema = st.number_input("12. Do you have edema?")
    Creatinine = st.number_input("14. Enter your Creatinine level")
    GFR = st.number_input("16. Enter your GFR level")
    Leukemia = st.number_input("18. Enter your Leukemia level")

# Predict button
if st.button("Predict"): 
    result = prediction(Age, gender, height, weight, bmi, bp_hi, bp_lo, cholesterol, glucose, smoke, alcohol, edema, jaundice, Creatinine, Creatinine_clearance, GFR, Polycythemia, Leukemia) 
    st.success(f"The prediction result is: {result}")



 

   

    
    


