from src.data_loader import load_survey_data

file_path = 'data/raw/survey_results.xlsx'
df22, df23 = load_survey_data(file_path)

print("df22 shape:", df22.shape)
print("df23 shape:", df23.shape)
