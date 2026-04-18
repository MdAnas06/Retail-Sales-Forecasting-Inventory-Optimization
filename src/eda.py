import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(df):
    print("\n--- EDA STARTED ---")

    # Basic info
    print("\nData Info:")
    print(df.describe())

    # Plot 1: Sales over time
    plt.figure(figsize=(12,5))
    plt.plot(df['date'], df['sales'])
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("images/sales_trend.png")
    plt.show()

    # Plot 2: Distribution
    plt.figure(figsize=(8,5))
    sns.histplot(df['sales'], bins=30, kde=True)
    plt.title("Sales Distribution")
    plt.savefig("images/sales_distribution.png")
    plt.show()

    # Add time-based features
    df['day_of_week'] = df['date'].dt.day_name()
    df['month'] = df['date'].dt.month

    # Plot 3: Weekly pattern
    plt.figure(figsize=(10,5))
    sns.boxplot(x='day_of_week', y='sales', data=df,
                order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    plt.title("Sales by Day of Week")
    plt.xticks(rotation=30)
    plt.savefig("images/weekly_pattern.png")
    plt.show()

    # Plot 4: Monthly trend
    plt.figure(figsize=(10,5))
    sns.barplot(x='month', y='sales', data=df)
    plt.title("Average Monthly Sales")
    plt.savefig("images/monthly_sales.png")
    plt.show()

    print("\n--- EDA COMPLETED ---")

    return df
def generate_insights(df):
    print("\n--- BUSINESS INSIGHTS ---")

    avg_sales = df['sales'].mean()
    max_sales = df['sales'].max()
    min_sales = df['sales'].min()

    print(f"Average Sales: {avg_sales:.2f}")
    print(f"Max Sales: {max_sales:.2f}")
    print(f"Min Sales: {min_sales:.2f}")

    peak_day = df.groupby('day_of_week')['sales'].mean().idxmax()
    print(f"Peak Sales Day: {peak_day}")

    return
