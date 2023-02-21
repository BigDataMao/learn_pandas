# coding=utf8
import pandas as pd
import json

# 嵌套的json,常见
json_nested = pd.read_json('../data/input/json/nested_list.json')
df = pd.DataFrame(json_nested)
print(df, '\n\n')

# 如何展平,先使用json模块载入文件
with open('../data/input/json/nested_list.json') as f:
    data = json.load(f)
    # data = json.loads(f.read()) 亦可
print(data, '\n\n')

# 把json里面的student展平,!!!但是信息不全
stu_normalized = pd.json_normalize(data, record_path=['students'])
print(stu_normalized, '\n\n')

# 展平的同时,使用meta包含全部元信息
full_normalized = pd.json_normalize(data,
                                    record_path=['students'],
                                    meta=['school_name', 'class'])
print(full_normalized, '\n\n')

