import pandas as pd
import numpy as np

def generate_sales_data():
    np.random.seed(42)

    dates = pd.date_range(start='2023-01-01', periods=365)

    # Trend (increasing sales over time)
    trend = np.linspace(10, 50, 365)

    # Seasonality (weekly pattern)
    seasonality = 10 + 5 * np.sin(2 * np.pi * dates.dayofyear / 7)

    # Noise
    noise = np.random.normal(0, 3, 365)

    sales = trend + seasonality + noise
    sales = np.maximum(0, sales)  # avoid negative

    df = pd.DataFrame({
        'date': dates,
        'sales': sales.round(2)
    })

    return df


if __name__ == "__main__":
    df = generate_sales_data()
    df.to_csv("data/raw/sales.csv", index=False)
    print("Dataset created successfully!")