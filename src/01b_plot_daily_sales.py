import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/daily_sales.csv")
df["date"] = pd.to_datetime(df["date"])

plt.figure()
plt.plot(df["date"], df["sales"])
plt.title("Daily Total Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()
