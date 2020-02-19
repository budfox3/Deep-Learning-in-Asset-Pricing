import pandas as pd

df = pd.read_csv('/mydata/realZ_sample.csv')

df.head().to_csv('result.csv')