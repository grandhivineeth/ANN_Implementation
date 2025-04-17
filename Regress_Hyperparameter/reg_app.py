import streamlit as st 
import pandas as pd 
import numpy as np 
import tensorflow as tf
import pickle 

## Load the trained model 
model = tf.keras.models.load_model('regression_model.h5')

## Loading the encoders and scalers 
with open('onehot_encoder_con_reg.pkl', 'rb') as file: 
    label_encoder_geo = pickle.load(file)

with open('label_encoder_gen_reg.pkl', 'rb') as file: 
    label_encoder_gender = pickle.load(file)

with open('scaler_reg.pkl', 'rb') as file: 
    scaler = pickle.load(file)

## streamlit app 
st.title('Estimated Salary Prediction') 

## User input 
country = st.selectbox('Country', label_encoder_geo.categories_[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance', min_value= 0, max_value= 260000)
credit_score = st.number_input('Credit Score',  min_value= 350, max_value= 850)
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])
churn = st.selectbox('Churn', [0,1])

# Prepare the input data 
input_data = pd.DataFrame({
    'credit_score': [credit_score], 
    'gender': [label_encoder_gender.transform([gender])[0]], 
    'age': [age], 
    'tenure': [tenure], 
    'balance': [balance],
    'products_number': [num_of_products], 
    'credit_card': [has_cr_card], 
    'active_member': [is_active_member],
    'churn': [churn]
})

# One-hot code
geo_encoded = label_encoder_geo.transform([[country]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=label_encoder_geo.get_feature_names_out(['country']))

# Combine one-hot with input data 
input_data = pd.concat([input_data.reset_index(drop= True), geo_encoded_df], axis= 1)

# scale the input data 
input_data_scaled = scaler.transform(input_data)

# prediction 
prediction = model.predict(input_data_scaled)
pred_salary = prediction[0][0]
st.write(f'Predicted Salary: ${pred_salary: .2f}')