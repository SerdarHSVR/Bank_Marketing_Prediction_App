import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open('best_model.pkl', 'rb'))

def predict(model, input_df):
    prediction = model.predict(input_df)
    return prediction[0]

def main():

    st.set_page_config(page_title="Bank Marketing Prediction App'", page_icon=":bank:", layout="centered")
    st.title("📊 Bank Marketing Prediction App")
    st.write("Fill in the details below to predict whether a client will subscribe to a term deposit.")

        # Sidebar section
    st.sidebar.title("📘 Project Info")
    st.sidebar.markdown("""
    **👤 Developer:** Serdar Hoşver  
    **🏫 University:** TED University  
    **📚 Course:** ADS542 – Statistical Learning  
    **👨‍🏫 Instructor:** Dr. Hakan Emekci  

    ---

    ### 🧠 Project Overview

    This Streamlit application is built as part of the final project for the **ADS542 - Statistical Learning** course. It uses machine learning techniques to **predict whether a customer will subscribe to a term deposit**, based on their demographic, financial, and interaction history with the bank.

    - **Dataset:** Bank Marketing Dataset 
    - **Model Used:** Random Forest Classifier  
    - **Classification Goal:** Predict the binary outcome (`yes` / `no`) for term deposit subscription.

    ---

    ### 🚀 Key Project Steps

    - Data Cleaning & Preprocessing  
    - Feature Selection  
    - Model Comparison (Logistic Regression, Neural Network, Random Forest)  
    - Hyperparameter Tuning  
    - Final Model Deployment with Streamlit

    ---

    ### 🔗 Useful Info

    - [UCI Dataset Source](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)

    ---
    **📬 Contact:**  
    [LinkedIn](www.linkedin.com/in/serdarhosver) • [Email](mailto:serdarhosver4@gmail.com) • [Github](https://github.com/SerdarHSVR)
    """)

    with st.expander("🧑 Client Personal Information"):
        age = st.number_input('Age', min_value=18, max_value=100, value=30)
        job = st.selectbox('Job', options=["blue-collar", "services", "admin.", "entrepreneur", "self-employed", "technician", "management", "student", "retired", "housemaid", "unemployed"])
        marital = st.selectbox('Marital Status', options=["married", "single", "divorced"])
        education = st.selectbox('Education Level', options=["basic.9y", "high.school", "university.degree", "professional.course", "basic.6y", "basic.4y", "illiterate"])

    with st.expander("🏦 Credit and Loan Information"):
        default = st.radio('Has Credit in Default?', ["no", "yes"])
        housing = st.radio('Has Housing Loan?', ["no", "yes"])
        loan = st.radio('Has Personal Loan?', ["no", "yes"])

    with st.expander("📞 Contact and Campaign Details"):
        contact = st.selectbox('Contact Communication Type', options=["cellular", "telephone"])
        month = st.selectbox('Last Contact Month', options=["may", "jun", "nov", "sep", "jul", "aug", "mar", "oct", "apr", "dec"])
        day_of_week = st.selectbox('Last Contact Day', options=["mon", "tue", "wed", "thu", "fri"])
        duration = st.slider('Last Contact Duration (seconds)', 0, 5000, step=10)
        campaign = st.number_input('Number of Contacts in Current Campaign', min_value=0, step=1)
        pdays = st.number_input('Days Since Last Contact (-1 if not previously contacted)', value=999)
        previous = st.number_input('Number of Previous Contacts', min_value=0, step=1)
        poutcome = st.selectbox('Outcome of Previous Campaign', options=["nonexistent", "failure", "success"])

    with st.expander("📈 Economic Indicators"):
        emp_var_rate = st.number_input('Employment Variation Rate', format="%.2f")
        cons_price_idx = st.number_input('Consumer Price Index (CPI)', format="%.2f")
        cons_conf_idx = st.number_input('Consumer Confidence Index', format="%.2f")
        euribor3m = st.number_input('Euribor 3 Month Rate', format="%.3f")
        nr_employed = st.number_input('Number of Employees', format="%.1f")

    # User input preview
    user_data = {
        'age': age,
        'job': job,
        'marital': marital,
        'education': education,
        'default': default,
        'housing': housing,
        'loan': loan,
        'contact': contact,
        'month': month,
        'day_of_week': day_of_week,
        'duration': duration,
        'campaign': campaign,
        'pdays': pdays,
        'previous': previous,
        'poutcome': poutcome,
        'emp.var.rate': emp_var_rate,
        'cons.price.idx': cons_price_idx,
        'cons.conf.idx': cons_conf_idx,
        'euribor3m': euribor3m,
        'nr.employed': nr_employed
    }

    features = pd.DataFrame(user_data, index=[0])

    st.subheader("🔍 Preview of Your Input")
    st.dataframe(features)

    if st.button("💡 Predict Outcome"):
        prediction = predict(model, features)
        if prediction == 0:
            st.error("❌ The client is unlikely to subscribe to the term deposit.")
        else:
            st.success("✅ The client is likely to subscribe to the term deposit.")

if __name__ == "__main__":
    main()
