# 🧠 Customer Churn Prediction using Artificial Neural Network (ANN)

This project is a simple yet powerful web application that predicts whether a customer will **churn** (i.e., leave the bank) based on key behavioral and demographic features. Built using an **Artificial Neural Network (ANN)** model trained on the classic **Churn Modelling** dataset, the app offers a fast and interactive way to test predictions via a sleek user interface.

## 🚀 Live Demo

👉 [🔗 Click here to try the app](https://annimplementation.streamlit.app)  
*(Hosted with Streamlit Cloud)*

## 📦 GitHub Repository

📂 [View on GitHub](https://github.com/grandhivineeth/ANN_Implementation.git)

## 📌 About the Project

- 🧠 Built an ANN using `Keras` and `TensorFlow` for binary classification.
- 📊 Trained on a dataset containing 10,000 bank customer records.
- 🌐 Deployed as an interactive web app using `Streamlit`.
- 🧪 Provides real-time prediction based on user input.

## 📁 Features

- Accepts user input for customer attributes like:
  - Credit Score
  - Age
  - Tenure
  - Balance
  - Number of Products
  - Active Membership
  - Estimated Salary
  - Geography & Gender
- Returns whether the customer is likely to churn or not.
- Shows prediction probability.

## 🧰 Tech Stack

| Layer        | Tools & Frameworks                             |
|--------------|------------------------------------------------|
| ML Model     | Python, Pandas, NumPy, Keras, TensorFlow       |
| Frontend     | Streamlit                                      |
| Deployment   | Streamlit Cloud / GitHub Pages                 |

## 🗂️ Folder Structure
```
  |-- ANN_Implementation 
    |-- app.py - Streamlit frontend app 
    |-- Bank_Customer_Churn_Prediction.csv - Data with which the ANN is trained 
    |-- experiment.ipynb - Trained model 
    |-- label_encoder_gender.pkl - Pickle for encoding gender 
    |-- model.h5 - Trained model stored in .h5 format 
    |-- onehot_encoder_geo.pkl - Pickle for onehot encoding country 
    |-- scaler.pkl - Pickle for scaling the data 
    |-- requirements.txt - Requirements for deploying the application
    |-- README.md - Hey!, it's me!
```  
## 📦 Setup Instructions

- **Clone the repository**

```bash
git clone https://github.com/grandhivineeth/ANN_Implementation.git
cd customer-churn-ann
```

- **Install dependencies**

```
pip install -r requirements.txt
```

- **Run the Streamlit app**

```
streamlit run app.py
```
This process is for deploying the application in your local machine. 

## ✅ Model Performance 

- Accuracy: 81% on validation data
- Evaluated using accuracy, Optmizer using "Adam", Loss using "Binary CrossEntropy"

## ⭐ Acknowledgements

- Dataset Source: [🔗 Kaggle](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset)
- Udemy Course by [🧑‍💻 Krish Naik](https://www.krishnaik.in/)

## ✍️ Author 

**Sai Vineeth Grandhi** 

📞 **Let's connect:**  

📧 [Email](grandhisaivineeth@gmail.com) 

🔗 [LinkedIn](https://www.linkedin.com/in/saivineeth-grandhi/) 

📲 [Mobile]((716) 907-3618) 
