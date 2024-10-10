
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.utils.class_weight import compute_class_weight
import joblib

def evaluate_performance():
   
    df = pd.read_csv('heart.csv')
    

    df['age_chol_ratio'] = df['age'] / df['chol'].replace(0, np.nan)  
    df = df.dropna()  

  
    X = df.drop('target', axis=1)  
    y = df['target']  

   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    
    class_weights = compute_class_weight('balanced', classes=y.unique(), y=y)
    class_weight_dict = dict(zip(y.unique(), class_weights))

    
    param_grid = {
        'n_estimators': [50, 100, 150],
        'max_features': ['sqrt', 'log2', None],  
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'class_weight': [class_weight_dict, None]  
    }

    
    rf = RandomForestClassifier(random_state=42)


    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)


    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    y_pred = best_model.predict(X_test)

    print("Model performance metrics:")
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    
    cv_scores = cross_val_score(best_model, X, y, cv=5)
    print(f"Cross-Validation Accuracy: {cv_scores.mean():.2f} ± {cv_scores.std():.2f}")

evaluate_performance()
