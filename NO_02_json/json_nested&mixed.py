# coding=utf8
import json

import pandas as pd

with open('../data/input/json/nested_mix.json') as f:
    data = json.load(f)
print(data, '\n\n')

# meta参数为数组,可以二维
df = pd.json_normalize(data,
                       record_path='students',
                       meta=['class',
                             ['info', 'president'],
                             ['info', 'address']])
print(df, '\n\n')

# 单纯提取名字+数学成绩
# 注意:data['students']是可迭代对象,是数组才能这样迭代
for i in data['students']:
    print(i['name'],i['math'])

