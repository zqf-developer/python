from numpy import *
"""
曼哈顿距离也称为城市街区距离，数学定义如下：
d_{12} =\sum_{k=1}^{n}{left| x_{1k}-x_{2k} right| } 
"""
vector1 = mat([1, 2, 3])
vector2 = mat([4, 5, 6])
print(sum(abs(vector1-vector2)))

# 欧氏距离其实就是L2范数
print(sqrt((vector1-vector2)*(vector1-vector2).T))
