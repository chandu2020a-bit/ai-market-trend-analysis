import pandas as pd

df = pd.read_csv("data/stores.csv")
df.columns = df.columns.str.lower()

print(df.head())
print(df.describe())

df.to_parquet("data/stores_cleaned.parquet", index=False)
