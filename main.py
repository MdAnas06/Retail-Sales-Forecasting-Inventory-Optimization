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
from src.preprocessing import preprocess_data, validate_data
from src.eda import perform_eda

# Load & clean
df = preprocess_data("data/raw/sales.csv")
df = validate_data(df)

# EDA
df = perform_eda(df)

# Save processed data
df.to_csv("data/processed/clean_sales.csv", index=False)
from src.eda import perform_eda, generate_insights

df = perform_eda(df)
generate_insights(df)