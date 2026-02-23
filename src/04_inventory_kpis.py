import pandas as pd
import numpy as np

df = pd.read_csv("data/processed/daily_sales.csv")
daily = df["sales"]

avg = daily.mean()
std = daily.std()

lead_time_days = 7
z = 1.65  # ~95% service level

safety_stock = z * std * np.sqrt(lead_time_days)
reorder_point = (avg * lead_time_days) + safety_stock

out = pd.DataFrame([{
    "avg_daily_demand": round(avg, 2),
    "std_daily_demand": round(std, 2),
    "lead_time_days": lead_time_days,
    "service_level_z": z,
    "safety_stock": round(safety_stock, 2),
    "reorder_point": round(reorder_point, 2),
    "reorder_point_if_demand_plus_15pct": round(((avg * 1.15) * lead_time_days) + safety_stock, 2)
}])

out.to_csv("outputs/inventory_kpis.csv", index=False)
print(out)
print("✅ Saved outputs/inventory_kpis.csv")
