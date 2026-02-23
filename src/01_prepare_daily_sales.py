import pandas as pd
from pathlib import Path

RAW = Path("data/raw/sales.csv")
OUT = Path("data/processed/daily_sales.csv")

# Read only the columns we need (fast + less memory)
df = pd.read_csv(RAW, usecols=["date", "sales"])

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date", "sales"])

# Total daily sales across all stores & families
daily = df.groupby("date", as_index=False)["sales"].sum()
daily = daily.sort_values("date")

OUT.parent.mkdir(parents=True, exist_ok=True)
daily.to_csv(OUT, index=False)

print("✅ Saved:", OUT)
print(daily.head())
print(daily.tail())
print("Rows:", len(daily))

