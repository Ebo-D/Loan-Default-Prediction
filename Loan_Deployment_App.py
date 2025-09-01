import pandas as pd
import streamlit as st
import joblib 
from datetime import datetime

model = joblib.load("loan_default_and_repayment_prediction_model.pkl")

st.title('LOAN DEFAULT AND REPAYMENT PREDICTION')

systemloanid = st.number_input('systemloanid',  300000000.0, 310000000.0, 301994762.0)
loannumber = st.slider('loannumber', 1, 20, 12)
totaldue =  st.number_input('totaldue($)', 1000.0, 50000.0, 34500.0)

On_Time_Repayment =  st.slider('On_Time_Repayment', 0.0, 15.0, 7.0)
Late_Time_Repayment = st.slider('Late_Time_Repayment', 0.0, 10.0, 4.0)

 
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

if st.button('Predict Loan Default and Repayment Status'):
    data = {
        'systemloanid': [systemloanid],
        'loannumber': [loannumber],
        'totaldue': [totaldue],
        'On_Time_Repayment': [loannumber],
        'Late_Time_Repayment': [Late_Time_Repayment],
        'approveddate_year': [ approveddate_year],
        'approveddate_month': [ approveddate_month],
        'approveddate_day': [ approveddate_day],
        'approveddate_hour': [approveddate_hour],
        'approveddate_minute': [ approveddate_minute],
        'creationdate_year': [creationdate_year],
        'creationdate_month': [creationdate_month],
        'creationdate_day': [creationdate_day],
        'creationdate_hour': [creationdate_hour],
        'creationdate_minute': [creationdate_minute]
}
    
    df = pd.DataFrame(data)
    Loan_Repayment = model.predict(df) [0]
    
    st.success(f'Loan Default and Repayment Status: {Loan_Repayment}')