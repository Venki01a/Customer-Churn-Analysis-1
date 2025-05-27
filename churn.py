import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
from sklearn.preprocessing import LabelEncoder

# Function to set background image with a dark overlay
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(
                rgba(0, 0, 0, 0.6), 
                rgba(0, 0, 0, 0.6)
            ), url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background
set_background("Customer churn.png")

# Load the trained model
with open('Customer_churn_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the scaler
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Load dataset for Label Encoding
data = pd.read_csv('Churn_Modelling.csv')

# Function to preprocess user input
def preprocess_input(input_data):
    input_array = np.array([
        input_data['CreditScore'],
        input_data['Age'],
        input_data['Tenure'],
        input_data['Balance'],
        input_data['NumOfProducts'],
        input_data['EstimatedSalary']
    ])
    
    input_array = input_array.reshape(1, -1)
    
    # Scale the input using the loaded scaler
    input_scaled = scaler.transform(input_array)
    
    return input_scaled

# Streamlit UI
st.title("Customer Churn Prediction App")
st.subheader("Predict if a customer will churn (using XGBoost + Scaler)")

# Input fields
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, step=1)
age = st.number_input("Age", min_value=18, max_value=100, step=1)
tenure = st.number_input("Tenure", min_value=0, max_value=10, step=1)
balance = st.number_input("Balance", min_value=0.0, step=100.0)
num_of_products = st.number_input("Num of Products", min_value=1, max_value=4, step=1)
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, step=1000.0)

# Predict button
if st.button("Predict Churn"):
    input_dict = {
        'CreditScore': credit_score,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts': num_of_products,
        'EstimatedSalary': estimated_salary
    }
    
    processed_input = preprocess_input(input_dict)
    prediction = model.predict(processed_input)
    
    if prediction[0] == 1:
        st.error("The customer is likely to churn.")
    else:
        st.success("The customer is likely to stay.")
