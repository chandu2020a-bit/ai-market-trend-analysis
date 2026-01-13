import pandas as pd

df = pd.read_parquet("data/stores_cleaned.parquet")

print("\nStore Type Count:")
print(df['type'].value_counts())

print("\nAverage Size by Store Type:")
print(df.groupby('type')['size'].mean().sort_values(ascending=False))
