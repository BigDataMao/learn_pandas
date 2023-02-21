# coding=utf8
import pandas as pd

df = pd.read_csv('../data/input/clean_clear/property-data.csv')
print(df,'\n\n')

# 均值填充
mid = df['ST_NUM'].mean().round(1)
df['ST_NUM'].fillna(mid,inplace=True)
print(df, '\n\n')