# AI-Powered Healthcare Disease Prediction and Clinical Analytics Platform

## Project Overview

The **AI-Powered Healthcare Disease Prediction and Clinical Analytics Platform** is a machine learning-based web application developed to predict the likelihood of heart disease based on patient health parameters.

The system uses a trained **Naive Bayes machine learning model** to generate disease predictions, disease probability, risk categories, and predictive insights.

The application is deployed using **Flask and Railway**, with prediction data stored in a **Railway MySQL database** and analyzed using **Microsoft Power BI**.


## Objectives

- Predict the likelihood of heart disease using Machine Learning.
- Calculate the probability of heart disease.
- Classify patients into Low, Moderate, and High Risk categories.
- Provide feature-based predictive insights.
- Store prediction results in a MySQL database.
- Deploy the application on the cloud.
- Analyze prediction data using Power BI.


## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- MySQL
- MySQL Connector
- Joblib
- HTML
- CSS
- Railway
- Microsoft Power BI
- Jupyter Notebook

---

## Machine Learning

The project uses the **UCI Heart Disease Dataset**.

Several machine learning algorithms were evaluated:

| Model | Accuracy |
|---|---:|
| Logistic Regression | 86.89% |
| K-Nearest Neighbors | 88.52% |
| Support Vector Machine | 85.25% |
| Decision Tree | 73.77% |
| Random Forest | 88.52% |
| Naive Bayes | 86.89% |

After model evaluation, **Naive Bayes** was selected as the final model for deployment.


## Input Features

The application accepts the following 13 patient parameters:

1. Age
2. Sex
3. Chest Pain Type
4. Resting Blood Pressure
5. Cholesterol
6. Fasting Blood Sugar
7. Resting ECG
8. Maximum Heart Rate
9. Exercise-Induced Angina
10. Oldpeak
11. Slope
12. CA
13. Thal


## System Workflow

Patient Input
      ↓
Flask Web Application
      ↓
Data Preprocessing
      ↓
Naive Bayes ML Model
      ↓
Heart Disease Prediction
      ↓
Disease Probability
      ↓
Risk Classification
      ↓
Predictive Insights
      ↓
Railway MySQL Database
      ↓
Power BI Dashboard


## Web Application

The Flask web application allows users to enter patient health information and receive a prediction.

Application Process
User enters patient information.
Flask receives the input.
Input data is converted into the required format.
The trained ML pipeline processes the data.
The model generates a prediction.
Disease probability is calculated.
Risk category is determined.
Predictive insights are generated.
Prediction details are stored in MySQL.
The result is displayed on the web page.

## Database

The application uses MySQL to store prediction results.

The main table is:

predictions

The table contains:

prediction_id
age
sex
cp
trestbps
chol
fbs
restecg
thalach
exang
oldpeak
slope
ca
thal
prediction
prediction_result
prediction_probability
risk_category
prediction_date

Each time a user performs a prediction, the patient information and prediction result are stored in the database.

## Cloud Deployment

The application is deployed using Railway.

The Flask application and MySQL database are connected through Railway.

Database credentials are stored using environment variables instead of directly exposing them in the source code.

Environment variables used include:

MYSQLHOST
MYSQLPORT
MYSQLUSER
MYSQLPASSWORD
MYSQLDATABASE


## Power BI Integration

The prediction database is connected to Microsoft Power BI for clinical analytics and visualization.

Power BI is used to analyze the prediction records stored in the MySQL database.

Dashboard Metrics

The dashboard includes analysis such as:

Total Predictions
Heart Disease Cases
No Heart Disease Cases
Average Disease Probability
High Risk Patients
Moderate Risk Patients
Low Risk Patients
Age-wise Risk Analysis
Cholesterol Analysis
Blood Pressure Analysis
Risk Category Distribution


## 📁 Project Structure
AI_Healthcare_Heart_Disease/
│
├── app.py
├── requirements.txt
├── heart_disease_naive_bayes_model.pkl
│
├── datasets/
│   └── heart_disease_clean.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_sql_connector.ipynb
|   |__ 05_feature_engineering.ipynb
│
├── templates/
│   └── index.html
│   
│
└── README.md

## Installation
1. Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Navigate to the Project Folder
cd AI_Healthcare_Heart_Disease
3. Install Required Libraries
pip install -r requirements.txt
4. Run the Application
python app.py

The application will be available at:

https://aihealthcarepredictionsystem-production.up.railway.app/
Testing

The application was tested using different patient profiles, including:

Low-risk patients
Moderate-risk patients
High-risk patients
High cholesterol cases
High blood pressure cases
Low maximum heart rate cases
Exercise-induced angina cases
Elevated oldpeak cases
Different age groups

The prediction results are stored automatically in the MySQL database.

## Key Features
Machine Learning
Data preprocessing
Exploratory Data Analysis
Multiple ML model comparison
Naive Bayes model training
Model evaluation
Probability prediction
Web Application
Patient input form
Real-time prediction
Disease probability
Risk classification
Predictive insights
Decision support information
Database
MySQL database
Automatic prediction storage
Patient prediction history
Cloud database using Railway
Business Intelligence
Power BI integration
Interactive dashboards
Risk analysis
Patient analytics
Prediction trend analysis
