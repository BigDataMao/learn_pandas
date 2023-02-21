# coding=utf-8
import pandas as pd

# json格式的文本
json_data = [
    {'name': 'mao', 'age': 20, 'salary': 10000},
    {'name': 'xin', 'age': 21, 'salary': 15000},
    {'name': 'wei', 'age': 22, 'salary': 20000}
]

df = pd.DataFrame(json_data)
print(df, '\n\n')

# dic格式文本
dic_data = {
    'name': {'row01': 'mao', 'row02': 'xin', 'row03': 'wei'},
    'age': {'row01': 20, 'row02': 21, 'row03': 22},
    'salary': {'row01': 10000, 'row02': 15000, 'row03': 20000}
}

df2 = pd.DataFrame(dic_data)
print(df2, '\n\n')

# 类似
dic_data2 = {
    'name': ['mao', 'xin', 'wei'],
    'age': [20, 21, 22],
    'salary': [10000, 15000, 20000]
}
print(pd.DataFrame(dic_data2, index=[f'第{i:02d}行' for i in range(1, 4)]), '\n\n')
