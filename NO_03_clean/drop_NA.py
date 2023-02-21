# coding=utf8
import pandas as pd

df = pd.read_csv('../data/input/clean_clear/property-data.csv')

# 默认清洗很多种  '',' ',NA,n/a,NaN等等
new_df = df.dropna()
print(new_df.to_string())

# 最好自己额外指定
df2 = pd.read_csv('../data/input/clean_clear/property-data.csv',
                  na_values=['--','missing'])
print(df2.dropna().to_string())

# 指定哪列有空值
df3 = df.dropna(subset='PID')
print(df3)

# 空值填充
df4 = df.fillna('missing')
print(df4)

