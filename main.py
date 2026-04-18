import pandas as pd

df = pd.read_csv("data/raw/sales.csv")

print(df.head())
print("\nDataset Shape:", df.shape)
from src.preprocessing import preprocess_data

df = preprocess_data("data/raw/sales.csv")

print("\nCleaned Data Preview:\n")
print(df.head())

# Save processed data
df.to_csv("data/processed/clean_sales.csv", index=False)

print("\nProcessed data saved successfully!")