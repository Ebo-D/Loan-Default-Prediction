# Loan Default Prediction with Machine Learning  

This project predicts whether a loan will default using machine learning models.  
The target column in the dataset is **`good or bad flag`**, where:  
- `Good` → the loan is likely to be repaid  
- `Bad` → the loan is likely to default  

## Files in this Repository  
- `Loan_Default_Prediction.ipynb` → Jupyter notebook with data preprocessing, model training, and evaluation  
- `requirements.txt` → Python libraries needed to run the project 

## Libraries Used  
- pandas  
- numpy  
- scikit-learn  
- matplotlib  
- seaborn  
- scipy  
- imbalanced-learn  
- xgboost  
- lightgbm  

## Models Implemented  
- Logistic Regression  
- Decision Tree  
- Random Forest  
- XGBoost  
- LightGBM  

## Evaluation Metrics  
- Accuracy  
- Precision  
- Recall  
- F1 Score

##  Approach
- Exploratory Data Analysis (EDA)
- Feature engineering (encoding categorical columns, scaling numerical columns)
- Tried models: Logistic Regression, Random Forest, LightGBM, Decision Tree, XGBoost
- Evaluated with Accuracy, Precision, Recall, F1

## How to Run  

1. Clone this repository:  
   ```bash
   git clone https://github.com/Ebo-D/Loan-Default-Prediction.git
   cd Loan-Default-Prediction

2. install dependencies
   ```bash
   pip install -r requirements.txt

3. open the notebook
   ```bash
   jupyter notebook Loan_Default_Prediction.ipynb

## Results
-The dataset was imbalanced, so oversampling(SMOTE) was applied.While applied, it's to see it's working and not used in the testing of my dataset with my models and metrics

-Simpler models like Logistic Regression worked but didn’t perform as well.

-Random Forest gave the best balance of accuracy, Precision, Recall, and F1 Score with 78%

-These models are better at capturing default cases compared to the others.

## Deployment

-The model has been deployed for real-time predictions.

## Framework used: 
-Streamlit

## How to run
    ```bash
    streamlit run app.py
 
## Conclusion: 
-This project is part of my Data Science learning journey. The model will perform better if oversampling (SMOTE) is applied to my dataset and used dor the testing of the dataset.  
