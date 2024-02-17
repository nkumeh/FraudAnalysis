import pandas as pd

def load_data(filepath):
    """ Load data from CSV file into a Pandas DataFrame """
    return pd.read_csv(filepath)
