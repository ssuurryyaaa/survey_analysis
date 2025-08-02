import pandas as pd

def load_survey_data(file_path: str):
    """
    Loads 2022 and 2023 survey data into shorter-named DataFrames.
    
    Returns:
        df22: DataFrame for 2022
        df23: DataFrame for 2023
    """
    df22 = pd.read_excel(file_path, sheet_name='2022Anonymised Transformed Data')
    df23 = pd.read_excel(file_path, sheet_name='2023Anonymised Transformed Data')

    df22["Year"] = 2022
    df23["Year"] = 2023

    return df22, df23
