import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

def train_forecast_model(df):
    print("\n--- MODEL TRAINING STARTED ---")

    # Features & Target
    X = df[['lag_1', 'lag_7', 'rolling_mean_7', 'day_of_week', 'month']]
    y = df['sales']

    # Train-test split (time-based)
    split = int(len(df) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    # Model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")

    # Plot Actual vs Predicted
    plt.figure(figsize=(12,5))
    plt.plot(y_test.values, label='Actual')
    plt.plot(y_pred, label='Predicted')
    plt.title("Actual vs Predicted Sales")
    plt.legend()
    plt.savefig("images/forecast_vs_actual.png")
    plt.show()

    print("\n--- MODEL TRAINING COMPLETED ---")

    return model, X_test, y_test, y_pred