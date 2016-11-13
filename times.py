import pandas as pd
import numpy as np
import read
from dateutil.parser import parse

def get_hour(x):
    y = parse(x)
    return y.hour

if __name__ == "__main__":
    df = read.load_data()
    df['hour'] = df['submission_time'].apply(get_hour)
    
    print(df['hour'].value_counts().head)
    