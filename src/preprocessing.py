import pandas as pd

def preprocess_data(file_path):
    # Load data
    df = pd.read_csv(file_path)

    print("Initial Shape:", df.shape)

    # Convert date column
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Check missing values
    print("\nMissing Values Before:\n", df.isnull().sum())

    # Drop rows with invalid dates
    df = df.dropna(subset=['date'])

    # Fill missing sales values (forward fill)
    df['sales'] = df['sales'].ffill()

    # Sort by date
    df = df.sort_values('date')

    # Reset index
    df = df.reset_index(drop=True)

    print("\nMissing Values After:\n", df.isnull().sum())

    print("\nFinal Shape:", df.shape)

    return df


