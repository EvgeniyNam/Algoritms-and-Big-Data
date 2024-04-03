import pandas as pd

df = pd.read_csv('qm9.csv')
new_df = df.sample(n=20000, random_state=12)
new_df.to_csv('algs.csv')

