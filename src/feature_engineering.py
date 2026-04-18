import pandas as pd

def create_features(df):
    print("\n--- FEATURE ENGINEERING STARTED ---")

    # Lag features (previous sales)
    df['lag_1'] = df['sales'].shift(1)
    df['lag_7'] = df['sales'].shift(7)

    # Rolling mean (trend smoothing)
    df['rolling_mean_7'] = df['sales'].rolling(window=7).mean()

    # Time-based features
    df['day_of_week'] = df['date'].dt.dayofweek
    df['month'] = df['date'].dt.month

    # Drop rows with NaN (created due to lag)
    df = df.dropna()

    print("Feature Data Shape:", df.shape)
    print("\nFeature Columns:\n", df.columns)

    print("\n--- FEATURE ENGINEERING COMPLETED ---")

    return df
