import pandas as pd

def clean_data(df):
    """Clean and preprocess the DataFrame."""
    # Example: Remove rows with missing values
    df = df.dropna()
    
    # Example: Convert data types if necessary
    # df['some_column'] = df['some_column'].astype('int')
    
    return df
