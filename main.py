import pandas as pd

df = pd.read_csv("data/raw/sales.csv")

print(df.head())
print("\nDataset Shape:", df.shape)