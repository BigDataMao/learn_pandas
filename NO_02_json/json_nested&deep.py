# coding=utf8

import pandas as pd

# 读取为dataframe
df = pd.read_json('../data/input/json/nested_deep.json')

# 获取students列,apply()没法填参数
math_score = df['students']. \
    apply(lambda x: [x['name'], x['grade']['math']])
print(math_score)


# 先定义函数再写
def get_name_math(row):
    return row['name'], row['grade']['math']


# 得到元祖,变成列表,在变成dataframe
df01 = pd.DataFrame(df['students'].apply(get_name_math).tolist())
print(df01)


