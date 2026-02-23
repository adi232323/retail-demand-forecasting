import pandas as pd
from prophet import Prophet
from pathlib import Path

INP = Path("data/processed/daily_sales.csv")
OUT = Path("outputs/forecast_90_days.csv")

daily = pd.read_csv(INP)
daily["date"] = pd.to_datetime(daily["date"])

# Outlier guard (removes weird tiny days like 2013-01-01)
median_sales = daily["sales"].median()
daily = daily[daily["sales"] > 0.05 * median_sales]

prophet_df = daily.rename(columns={"date": "ds", "sales": "y"})

model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False
)

model.fit(prophet_df)

future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

out = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].rename(columns={"ds": "date"})

OUT.parent.mkdir(parents=True, exist_ok=True)
out.to_csv(OUT, index=False)

print("✅ Saved:", OUT)
print(out.tail())
