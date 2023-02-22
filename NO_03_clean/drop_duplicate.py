# coding=utf8
import pandas as pd
from p import p

df = pd.read_csv('../data/input/clean_clear/property-data.csv')
p(df, '\n\n')


# 直接删除某行,先创造布尔条件con,再用index进行drop
con = df.loc[df['ST_NUM'] > 200]
df.drop(con.index, inplace=True)
p(df, '\n\n')

# 造数据
data = {
    "name": ['Google', 'Sb', 'Sb', 'Taobao'],
    "age": [50, 40, 40, 23]
}
df2 = pd.DataFrame(data=data)
p(df2, '\n\n')

# 去重法一:布尔条件传给df,再drop
con = df2.loc[df2.duplicated()]
df3 = df2.drop(con.index)
p(df3, '\n\n')

# 去重法二:直接使用drop_duplicates
df2.drop_duplicates(inplace=True)
p(df2, '\n\n')
