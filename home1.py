import pandas as pd

df = pd.read_csv('dogs_dataset.csv')

print("\nПервые 5 строк данных:")
print(df.head())

print("\nИнформация о данных:")
print(df.info())

print("\nСтатистическое описание:")
print(df.describe())