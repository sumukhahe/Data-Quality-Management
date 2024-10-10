import time
from datetime import datetime
import pandas as pd
import numpy as np

def monitor_data_quality(df):
 
    z_scores = np.abs((df - df.mean()) / df.std())
    anomalies = (z_scores > 3).sum(axis=0)
    if anomalies.any():
        raise ValueError(f"Anomalies detected: {anomalies}")

def real_time_monitoring():
    while True:
     
        new_data = pd.read_csv('heart.csv')
        monitor_data_quality(new_data)
        print(f"Data quality monitored at {datetime.now()}")
        time.sleep(3600)  # Check every hour
