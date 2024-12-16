import streamlit as st
from prediction_helper import predict

# Add custom CSS for styling
st.markdown("""
    <style>
        /* Full-page light background image */
        body {
            background-image: url('htpexels-francesco-ungaro-998641.jpg');
            background-size: cover;
            background-attachment: fixed;
            color: #333333;
            font-family: 'Arial', sans-serif;
            margin-top: -50px; /* Shifting everything slightly upward */
        }

        /* Title styling */
        h1 {
            text-align: center;
            background: -webkit-linear-gradient(left, #6A5ACD, #48D1CC);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5em;
            font-weight: bold;
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        /* Input field styling */
        .stNumberInput > div, .stSelectbox > div {
            background: rgba(255, 255, 255, 0.85);
            border-radius: 6px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 8px;
            margin: 5px 0;
        }

        /* Button styling */
        .stButton > button {
            background: linear-gradient(to right, #4CAF50, #8BC34A);
            color: white;
            font-size: 14px;
            border-radius: 6px;
            border: none;
            padding: 15px 35px;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
        }

        .stButton > button:hover {
            background: linear-gradient(to right, #8BC34A, #4CAF50);
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown("<h1>Insurance Premium Predictor</h1>", unsafe_allow_html=True)

# Input Fields Layout
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Personal Information Section
row1 = st.columns(3)
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

# Health and Employment Section
row2 = st.columns(3)
with row2[0]:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

# Demographics Section
row3 = st.columns(3)
with row3[0]:
    gender = st.selectbox('Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

# Lifestyle Section
row4 = st.columns(3)
with row4[0]:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Button and Result in a Single Row
row5 = st.columns(2)
with row5[0]:
    if st.button('Predict'):
        prediction = predict(input_dict)
    else:
        prediction = ""

with row5[1]:
    st.markdown(f"""
        <div style='padding: 15px 20px; 
        background: rgba(255, 255, 255, 0.85); border-radius: 6px; font-size: 16px; color: #2E8B57;'>
            Predicted Health Insurance Cost:<strong> {prediction if prediction else 'Awaiting...'}</strong>
        </div>
    """, unsafe_allow_html=True)
