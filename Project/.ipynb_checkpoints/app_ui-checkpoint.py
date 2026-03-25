import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("Customer Churn Prediction App")

# Sidebar navigation
page = st.sidebar.selectbox("Select Page", ["Insights", "Prediction"])

# ------------------ INSIGHTS ------------------
if page == "Insights":
    st.header("📊 Business Insights")

    df = pd.read_csv("/Users/prajwalsubedi/Desktop/Data science/Data Sets/Telco_customer_churn.csv")

    st.write("Dataset Preview")
    st.dataframe(df.head())

    st.write("Churn Distribution")
    st.bar_chart(df['Churn Value'].value_counts())

# ------------------ PREDICTION ------------------
if page == "Prediction":
    st.header("🤖 Predict Churn")

    tenure = st.slider("Tenure Months", 0, 72, 12)
    monthly = st.slider("Monthly Charges", 0, 200, 70)

    if st.button("Predict"):
        input_df = pd.DataFrame({
            "Tenure Months": [tenure],
            "Monthly Charges": [monthly]
        })

        prob = model.predict_proba(input_df)[0][1]
        pred = 1 if prob > 0.3 else 0

        st.write(f"Churn Probability: {prob:.2f}")
        st.write(f"Prediction: {'Churn' if pred==1 else 'No Churn'}")