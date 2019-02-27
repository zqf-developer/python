import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer

# 读取csv文件
dataset = pd.read_csv('Data.csv')
# .iloc[行，列]
X = dataset.iloc[:, :-1].values
# : 全部行 or 列；[a]第a行 or 列 [a,b,c]第 a,b,c 行 or 列
Y = dataset.iloc[:, :-1].values
