import pandas as pd

prec = pd.read_csv('law_list_detail.csv', encoding='utf-8')

print(prec.shape)
print(prec.head())
print(prec.tail())
print(prec.info())
print(prec.isnull().sum())