import pandas as pd

def process_data(df: pd.DataFrame) -> list:
    """
    Cleans data (handling missing values) and prepares a structured input.
    Returns a list of dictionaries representing each area.
    """
    print("Processing data...")
    
    # Handle missing values: Fill missing numeric values with column mean
    # Or dropna. We will dropna for simplicity here.
    df_cleaned = df.dropna()
    
    # Ensure types are correct
    df_cleaned['temperature'] = pd.to_numeric(df_cleaned['temperature'])
    df_cleaned['tree_coverage'] = pd.to_numeric(df_cleaned['tree_coverage'])
    df_cleaned['building_density'] = pd.to_numeric(df_cleaned['building_density'])
    
    # Prepare structured input
    records = df_cleaned.to_dict(orient='records')
    return records
