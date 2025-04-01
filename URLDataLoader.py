import pandas as pd


df = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")

first_value = df.iloc[0, 0]
print("First cell value:", first_value)

