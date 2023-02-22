# coding=utf8
import pandas as pd
from p import p

df = pd.read_csv('../data/input/clean_clear/property-data.csv')
p(df, '\n\n')

# 均值填充所有
mid = df['ST_NUM'].mean().round(1)
df['ST_NUM'].fillna(mid, inplace=True)
p(df, '\n\n')

# 填充指定列
df['PID'].fillna('12345', inplace=True)
p(df, '\n\n')

# 修改某列全体格式
df['TIME'] = '20230101'
p(df, '\n\n')
df['TIME'] = pd.to_datetime(df['TIME'])
p(df, '\n\n')

# 修改单个数据
df.loc[4, 'PID'] = 100005000.0
p(df, '\n\n')

# 修改整列数据

# 法一:按行筛选赋值
df.loc[df['ST_NUM'] > 200, 'ST_NUM'] = 200
p(df, '\n\n')

# 法二:按行apply
df['ST_NUM'] = df['ST_NUM'].apply(lambda x: 199 if x > 199 else x)
p(df, '\n\n')

# 法三:按索引循环迭代,支持复杂语句
for i in df.index:
    if df.loc[i, 'ST_NUM'] > 198:
        df.loc[i, 'ST_NUM'] = 198
p(df, '\n\n')




