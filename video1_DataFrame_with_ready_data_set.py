import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')

print(df[df['Social support'] > 0.7])

#print(df.loc[56, 'Social support'])
#print(df.loc[56])

#print(df[['Country name', 'Regional indicator']])
#print(df['Country name'])

#print(df.head())
#print(df.tail())
#print(df.info())
#print(df.describe())

