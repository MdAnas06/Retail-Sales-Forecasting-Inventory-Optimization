import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def calculate_inventory_metrics(df, lead_time=5, service_level=1.65):
    print("\n--- INVENTORY CALCULATION STARTED ---")

    avg_demand = df['sales'].mean()
    demand_std = df['sales'].std()

    safety_stock = service_level * demand_std * np.sqrt(lead_time)
    reorder_point = (avg_demand * lead_time) + safety_stock

    print(f"Average Demand: {avg_demand:.2f}")
    print(f"Safety Stock: {safety_stock:.2f}")
    print(f"Reorder Point: {reorder_point:.2f}")

    print("\n--- INVENTORY CALCULATION COMPLETED ---")

    return avg_demand, safety_stock, reorder_point


def generate_inventory_plan(df, reorder_point):
    print("\n--- GENERATING INVENTORY PLAN ---")

    df['current_stock'] = 200 - df['sales'].cumsum()

    df['reorder_flag'] = df['current_stock'] < reorder_point

    df['recommended_order_qty'] = np.where(
        df['reorder_flag'],
        reorder_point - df['current_stock'],
        0
    )

    return df


def plot_inventory(df, reorder_point):
    plt.figure(figsize=(12, 5))

    plt.plot(df['date'], df['current_stock'], label='Stock Level')

    plt.axhline(y=reorder_point, linestyle='--', label='Reorder Point')

    plt.title("Inventory Level Over Time")
    plt.xlabel("Date")
    plt.ylabel("Stock Level")

    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("images/inventory_trend.png")
    plt.show()
    
    import matplotlib.pyplot as plt

def plot_inventory(df, reorder_point):
    plt.figure(figsize=(12,5))
    plt.plot(df['date'], df['current_stock'], label='Stock Level')
    plt.axhline(y=reorder_point, color='r', linestyle='--', label='Reorder Point')
    plt.title("Inventory Level Over Time")
    plt.legend()
    plt.savefig("images/inventory_trend.png")
    plt.show()