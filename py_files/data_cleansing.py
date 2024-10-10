from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import pandas as pd

def detect_outliers_iqr(df, column):
    
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    
    return outliers, lower_bound, upper_bound

def cleanse_data(df):
   
    imputer = SimpleImputer(strategy='median')
    df[['age', 'trestbps', 'chol', 'thalach', 'oldpeak']] = imputer.fit_transform(df[['age', 'trestbps', 'chol', 'thalach', 'oldpeak']])
    
  
    for column in ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']:
        outliers, lower_bound, upper_bound = detect_outliers_iqr(df, column)
        
        if not outliers.empty:
         
            df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
            

    scaler = StandardScaler()
    df[['age', 'trestbps', 'chol', 'thalach', 'oldpeak']] = scaler.fit_transform(df[['age', 'trestbps', 'chol', 'thalach', 'oldpeak']])
    
    print("Data cleansing and outlier handling completed")
    return df


df = pd.read_csv('heart.csv')
df = cleanse_data(df)
