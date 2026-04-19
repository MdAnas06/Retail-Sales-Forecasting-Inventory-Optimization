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
from src.preprocessing import preprocess_data, validate_data
from src.eda import perform_eda, generate_insights
from src.feature_engineering import create_features

# Step 1: Load & clean
df = preprocess_data("data/raw/sales.csv")
df = validate_data(df)

# Step 2: EDA
df = perform_eda(df)
generate_insights(df)

# Step 3: Feature Engineering
df = create_features(df)

# Save feature dataset
df.to_csv("data/processed/feature_data.csv", index=False)

print("\nFeature dataset saved successfully!")
df['rolling_std_7'] = df['sales'].rolling(7).std()


from src.preprocessing import preprocess_data, validate_data
from src.eda import perform_eda, generate_insights
from src.feature_engineering import create_features
from src.forecasting import train_forecast_model

# Step 1: Load & clean
df = preprocess_data("data/raw/sales.csv")
df = validate_data(df)

# Step 2: EDA
df = perform_eda(df)
generate_insights(df)

# Step 3: Feature Engineering
df = create_features(df)

# Step 4: Forecasting
model, X_test, y_test, y_pred = train_forecast_model(df)

# Save predictions
output = X_test.copy()
output['actual_sales'] = y_test.values
output['predicted_sales'] = y_pred

output.to_csv("outputs/forecast_results.csv", index=False)

print("\nForecast results saved successfully!")


from src.inventory import calculate_inventory_metrics, generate_inventory_plan
# Inventory calculations
avg_demand, safety_stock, reorder_point = calculate_inventory_metrics(df)

# Inventory planning
inventory_df = generate_inventory_plan(df, reorder_point)

# Save output
inventory_df.to_csv("outputs/inventory_plan.csv", index=False)

print("\nInventory plan saved successfully!")
from src.inventory import plot_inventory

plot_inventory(inventory_df, reorder_point)
from src.preprocessing import preprocess_data, validate_data
from src.eda import perform_eda, generate_insights
from src.feature_engineering import create_features
from src.forecasting import train_forecast_model
from src.inventory import calculate_inventory_metrics, generate_inventory_plan, plot_inventory

# Load & preprocess
df = preprocess_data("data/raw/sales.csv")
df = validate_data(df)

# EDA
df = perform_eda(df)
generate_insights(df)

# Feature engineering
df = create_features(df)

# Forecasting
model, X_test, y_test, y_pred = train_forecast_model(df)

# Inventory optimization
avg_demand, safety_stock, reorder_point = calculate_inventory_metrics(df)
inventory_df = generate_inventory_plan(df, reorder_point)

# Save outputs
df.to_csv("data/processed/feature_data.csv", index=False)
inventory_df.to_csv("outputs/inventory_plan.csv", index=False)

# Plot inventory
plot_inventory(inventory_df, reorder_point)

print("\n--- PIPELINE EXECUTED SUCCESSFULLY ---")