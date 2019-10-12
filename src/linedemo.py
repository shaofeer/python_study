import matplotlib.pyplot as plt

# data_x = [1, 2, 3, 4, 5]
# data_y = [1, 4, 9, 16, 25]
# plt.plot(data_x, data_y, linewidth=2)
# plt.title("Test", fontsize=20)
# plt.xlabel("m/s")
# plt.ylabel("c")
# plt.tick_params(axis='x',labelsize=20)
# plt.show()


# point_data_x = [1, 2, 4, 4, 5]
# point_data_y = [1, 2, 3, 4, 5]

# point_data_x = list(range(0, 100))
# point_data_y = [x ** 2 for x in point_data_x]

# RGB
# plt.scatter(point_data_x, point_data_y, s=40, c=(0, 0, 0))
# color
# plt.scatter(point_data_x, point_data_y, s=40, c='red')

# plt.axis([0, 100, 0, 200])


x_values = list(range(1001))
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# 展示图表
# plt.show()

# 保存图表
plt.savefig("b.png",bbox_inches='tight')
