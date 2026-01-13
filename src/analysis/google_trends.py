import pandas as pd

trends = pd.read_csv(
    "data/google_trends.csv",
    skiprows=3,              # <-- THIS IS THE FIX
    names=["date", "walmart_interest"]
)

# Convert columns safely
trends["date"] = pd.to_datetime(trends["date"], format="%Y-%m-%d")
trends["walmart_interest"] = pd.to_numeric(trends["walmart_interest"])

print("Last 5 rows:")
print(trends.tail())

print("\nAverage interest:")
print(trends["walmart_interest"].mean())

print("\nTrend direction (last vs first year):")
print(
    trends.tail(12)["walmart_interest"].mean()
    - trends.head(12)["walmart_interest"].mean()
)
