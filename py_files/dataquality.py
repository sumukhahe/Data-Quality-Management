import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def validate_data(df):
    """ Validate the data for missing values and correct data types. """
    # Check for missing values
    missing_values = df.isnull().sum()
    if missing_values.any():
        raise ValueError(f"Missing values detected: {missing_values}")

    # Check data types
    expected_types = {
        'age': 'int64',
        'sex': 'int64',
        'cp': 'int64',
        'trestbps': 'int64',
        'chol': 'int64',
        'fbs': 'int64',
        'restecg': 'int64',
        'thalach': 'int64',
        'exang': 'int64',
        'oldpeak': 'float64'
    }
    for column, dtype in expected_types.items():
        if df[column].dtype != dtype:
            raise TypeError(f"Column {column} should be of type {dtype}. Current type: {df[column].dtype}")

    print("Data validation successful")


def detect_outliers_iqr(df, column):
    """ Detect outliers in a specific column using the IQR method. """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    
    if not outliers.empty:
        print(f"Outliers detected in {column}:")
        print(outliers)
    else:
        print(f"No outliers detected in {column}.")

    return outliers


def process_data(file_path):
    """ Load and process data by validating and cleansing it. """
    df = pd.read_csv(file_path)
    validate_data(df)
    
    for column in ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']:
        detect_outliers_iqr(df, column)
    
    return df

df = process_data('heart.csv')