# 📊 Bank Marketing Campaign Prediction App

This project is developed as part of the **ADS542 - Statistical Learning** course at **TED University**, instructed by **Dr. Hakan Emekci**. The main objective is to build, evaluate, and deploy a classification model that predicts whether a client of a Portuguese bank will subscribe to a term deposit.

---

## 🧑‍💻 Author

**Serdar Hoşver**  
Graduate Student, TED University  
Course: ADS542 – Statistical Learning  
Instructor: Dr. Hakan Emekci  
Submission Date: May 12, 2025

---

## 📁 Project Description

This machine learning application uses the **Bank Marketing Dataset** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing) and focuses on predicting the target variable `y` (term deposit subscription) using direct marketing campaign data.

The dataset contains **4119 rows and 20 features**, including both **categorical and numerical variables**.

---

## 🔍 Dataset Summary

- **Source:** [UCI Bank Marketing Dataset](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)
- **CSV File Used:** `bank-additional.csv`
- **Target Variable:** `y` – whether the client subscribed to a term deposit

---

## 🧠 ML Workflow Overview

The project follows these machine learning steps:

1. **Data Cleaning & Preprocessing**
2. **Feature Encoding and Scaling**
3. **Model Training & Evaluation**  
   - Models used: `Logistic Regression`, `Random Forest`, `MLPClassifier`
4. **Hyperparameter Tuning (GridSearchCV)**
5. **Model Selection**
6. **Streamlit App Deployment**

---

## 🚀 Deployment

A fully interactive **Streamlit app** is included in this repository to allow real-time predictions based on user inputs. You can run it locally or deploy to Streamlit Cloud.

### To Run Locally:

1. Install dependencies:

```bash
pip install -r requirements.txt
