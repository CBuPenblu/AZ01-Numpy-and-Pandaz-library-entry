import pandas as pd

df = pd.read_csv('dz.csv')

average_salary = df.groupby('City')['Salary'].mean().reset_index()

print(average_salary)