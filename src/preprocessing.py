import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)

    print("Initial Shape:", df.shape)

    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    print("\nMissing Values Before:\n", df.isnull().sum())

    df = df.dropna(subset=['date'])

    # ✅ FIXED LINE (no deprecated method)
    df['sales'] = df['sales'].ffill()

    df = df.sort_values('date')
    df = df.reset_index(drop=True)

    print("\nMissing Values After:\n", df.isnull().sum())
    print("\nFinal Shape:", df.shape)

    return df


# ✅ MAKE SURE THIS EXISTS
def validate_data(df):
    print("\n--- DATA VALIDATION ---")

    negative_sales = df[df['sales'] < 0]
    print("Negative sales rows:", len(negative_sales))

    duplicates = df.duplicated().sum()
    print("Duplicate rows:", duplicates)

    date_diff = df['date'].diff().dt.days
    gaps = (date_diff > 1).sum()
    print("Date gaps found:", gaps)

    return df