# Pandas导入导出

import pandas as pd

data = pd.read_csv('student.csv')
print(data)

data.to_pickle('student.pickle')

# 需要其他格式可自行查找，兼容的格式有很多种


