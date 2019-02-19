import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 50))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='x', which='major', labelsize=14)
# plt.axes([0, 100, 0, 1100])

# 显示图像
plt.show()

# 保存图片到本路径 ,不能设置bbox_inches，否则导出会报错
# plt.savefig('squares_plot.png')
