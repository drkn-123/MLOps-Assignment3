import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

input_file = "news_data.csv"
output_file = "processed_data.csv"

if not os.path.exists(input_file):
    raise FileNotFoundError(f"{input_file} does not exist")

df = pd.read_csv(input_file)

df.dropna(inplace=True)

scaler = StandardScaler()

if "Temperature" in df.columns and "Wind Speed" in df.columns:
    df[["Temperature", "Wind Speed"]] = scaler.fit_transform(df[["Temperature", "Wind Speed"]])

df.to_csv(output_file, index=False)
print(f"Preprocessed data saved to {output_file}")
