import pandas as pd

actual = pd.read_csv("data/processed/daily_sales.csv")
forecast = pd.read_csv("outputs/forecast_90_days.csv")

actual["date"] = pd.to_datetime(actual["date"])
forecast["date"] = pd.to_datetime(forecast["date"])

merged = actual.merge(forecast, on="date", how="outer").sort_values("date")
merged.to_csv("outputs/dashboard_actual_vs_forecast.csv", index=False)

print("✅ Saved outputs/dashboard_actual_vs_forecast.csv")
print(merged.tail())
