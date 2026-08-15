import pickle
import streamlit as st

# Set page title
st.set_page_config(page_title="Water Prediction")

# Show title
st.title("Water Consumption Prediction")
st.write("Predict daily water usage using Machine Learning")

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Get user input
st.write("---")
st.write("Enter your household details:")

# Ask for family members
family_members = st.number_input("Family Members", min_value=1, max_value=10, value=3)

# Ask for bathrooms
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=5, value=2)

# Ask for washing machine
washing_machine = st.selectbox("Washing Machine?", ["No", "Yes"])

# Ask for garden
garden = st.selectbox("Garden?", ["No", "Yes"])

# Button to predict
st.write("---")
if st.button("Predict Water Usage"):
    # Convert Yes/No to 1/0
    if washing_machine == "Yes":
        washing_value = 1
    else:
        washing_value = 0
    
    if garden == "Yes":
        garden_value = 1
    else:
        garden_value = 0
    
    # Create list of features
    features = [[family_members, bathrooms, washing_value, garden_value]]
    
    # Get prediction from model
    prediction = model.predict(features)[0]
    
    # Show result
    st.write("---")
    st.write("**Result:**")
    st.success(f"Daily Water Usage: {round(prediction)} Litres")