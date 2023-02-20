import pandas as pd

df = pd.read_json("../data/input/json/sites.json")
print(df, '\n\n')

df.index = (['第一行', '第二行', '第三行'])
print(df)
