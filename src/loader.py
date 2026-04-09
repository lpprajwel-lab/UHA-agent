import pandas as pd
import os

def load_data(filepath: str) -> pd.DataFrame:
    """
    Loads data from a CSV file and validates the structure.
    """
    print("Loading data...")
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found at: {filepath}")
    
    df = pd.read_csv(filepath)
    
    # Validate structure
    required_columns = {'area', 'temperature', 'tree_coverage', 'building_density'}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise ValueError(f"Missing required columns in dataset: {missing}")
        
    return df
