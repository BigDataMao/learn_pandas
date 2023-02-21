# coding=utf8
import pandas as pd


def p():
    print(df, '\n\n')


df = pd.read_json("../data/input/json/sites.json")
p()

df.index = (['第一行', '第二行', '第三行'])
p()

df.index = range(1, 4, 1)
p()

a = []
for i in range(1, 4, 1):
    a.append(f'高级的第{i}行')
df.index = a
# 格式化输出,但是不整齐
print(f"{'id':<10}{'name':<10}{'likes':<10}{'url':<20}")
for index, row in df.iterrows():
    print(f"{row['id']:<10}"
          f"{row['name']:<10}"
          f"{row['likes']:<10}"
          f"{row['url']:<20}")

# 整齐的格式化,实际测试还是不整齐,放弃
# 据说有个prettytable包
from tabulate import tabulate

print(tabulate(df, headers=df.columns.tolist(),
               tablefmt='psql', stralign='left',
               numalign='left', showindex=False))
