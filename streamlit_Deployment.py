#import libraries
import pandas as pd
import streamlit as st
import joblib 
from datetime import datetime

#load trained model pipeline
model = joblib.load("loan_default_model.pkl")

#title of deployment
st.title('LOAN DEFAULT AND REPAYMENT PREDICTION')

st.write('Enter Loan Applicant Details:')

#input fields for customers
loannumber = st.slider('loannumber', 1, 20, 12)
loanamount = st.number_input('loanamount($)',  5000.0, 50000.0, 30000.0)

bank_account_type =  st.selectbox('bank_account_type', ['Other', 'Savings', 'NA', 'Current'])
bank_name_clients = st.selectbox('bank_name_clients', ['Diamond Bank', 'GT Bank', 'EcoBank', 'First Bank', 'NA','Access Bank', 'UBA', 'Union Bank', 'FCMB', 'Zenith Bank','Stanbic IBTC', 'Fidelity Bank', 'Wema Bank', 'Sterling Bank','Skye Bank', 'Keystone Bank', 'Heritage Bank', 'Unity Bank','Standard Chartered'])
employment_status_clients = st.selectbox('employment_status_clients',['Permanent', 'Unknown', 'Unemployed', 'Self-Employed', 'Student','Retired', 'Contract']) 

                                
On_Time_Repayment =  st.slider('On_Time_Repayment', 0.0, 15.0, 7.0)
Late_Time_Repayment = st.slider('Late_Time_Repayment', 0.0, 10.0, 4.0)

age = st.slider('Age', 10, 100, 48)
interest = st.number_input('interest($)', 500.0, 20000.0, 4500.0)

 
st.subheader('Approved Date and Time')
approveddate = st.date_input('Select Approved Date')
approvedtime = st.time_input('Select Approved Time', step = 60)
 
approved_dt = datetime.combine(approveddate, approvedtime)
 
approveddate_year = approved_dt.year
approveddate_month = approved_dt.month
approveddate_day = approved_dt.day
approveddate_hour = approved_dt.hour
approveddate_minute = approved_dt.minute



st.subheader('Creation Date and Time')
creationdate = st.date_input('Select Creation Date')
creationtime = st.time_input('Select Creation Time', step = 60)
 
creation_dt = datetime.combine(creationdate, creationtime)
 
creationdate_year = creation_dt.year
creationdate_month = creation_dt.month
creationdate_day = creation_dt.day
creationdate_hour = creation_dt.hour
creationdate_minute = creation_dt.minute


# Show formatted output with full date + time
st.write('Approved:', approveddate_year, approveddate_month, approveddate_day, approveddate_hour, approveddate_minute)

st.write('Created:', creationdate_year, creationdate_month, creationdate_day, creationdate_hour,creationdate_minute)

termdays_cat = st.selectbox('termdays_cat', ['short', 'medium', 'long'])

#Normalize categorical columns to lowercase
bank_account_type=bank_account_type.strip().lower()
bank_name_clients = bank_name_clients.strip().lower()
employment_status_clients = employment_status_clients.strip().lower()
termdays_cat = termdays_cat.strip().lower()

if st.button('Predict Loan Default and Repayment Status'):

#Dataframe for Prediction
    data = {
        'loannumber': [loannumber],
        'loanamount': [loanamount],
        'bank_account_type': [bank_account_type],
        'bank_name_clients': [bank_name_clients],
        'employment_status_clients': [employment_status_clients],
        'On_Time_Repayment': [On_Time_Repayment],
        'Late_Time_Repayment': [Late_Time_Repayment],
        'age': [age],
        'interest': [interest],
        'approveddate_year': [ approveddate_year],
        'approveddate_month': [ approveddate_month],
        'approveddate_day': [ approveddate_day],
        'approveddate_hour': [approveddate_hour],
        'approveddate_minute': [ approveddate_minute],
        'creationdate_year': [creationdate_year],
        'creationdate_month': [creationdate_month],
        'creationdate_day': [creationdate_day],
        'creationdate_hour': [creationdate_hour],
        'creationdate_minute': [creationdate_minute],
        'termdays_cat': [termdays_cat]
}
    
    df = pd.DataFrame(data)
    Loan_Repayment = model.predict(df) [0]
    
    st.success(f'Loan Default and Repayment Status: {Loan_Repayment}')
    



    
   
    