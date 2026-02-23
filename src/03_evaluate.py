import pandas as pd
import numpy as np

actual = pd.read_csv("data/processed/daily_sales.csv")
forecast = pd.read_csv("outputs/forecast_90_days.csv")

actual["date"] = pd.to_datetime(actual["date"])
forecast["date"] = pd.to_datetime(forecast["date"])

merged = actual.merge(forecast, on="date", how="inner")

y_true = merged["sales"].values
y_pred = merged["yhat"].values

mae = np.mean(np.abs(y_true - y_pred))
mape = np.mean(np.abs((y_true - y_pred) / np.maximum(y_true, 1e-6))) * 100

print("MAE:", round(mae, 2))
print("MAPE%:", round(mape, 2))
print("Days evaluated:", len(merged))

pd.DataFrame([{
    "MAE": round(mae, 2),
    "MAPE_percent": round(mape, 2),
    "n_days_evaluated": len(merged)
}]).to_csv("outputs/metrics.csv", index=False)

print("✅ Saved outputs/metrics.csv")
