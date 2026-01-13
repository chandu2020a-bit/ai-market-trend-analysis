import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_parquet("data/stores_cleaned.parquet")

df['type'].value_counts().plot(kind='bar', title='Store Type Distribution')
plt.xlabel('Store Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
