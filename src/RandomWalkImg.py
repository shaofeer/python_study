import matplotlib.pyplot as plt
from src.RandomWalk import RandomWalk

rw = RandomWalk(step_num=5000)

rw.fill_walk()


plt.plot(rw.x_list,rw.y_list,linewidth=10)


# color_list = list(range(rw.step_num))

# plt.scatter(rw.x_list, rw.y_list, cmap=plt.cm.Blues, c=color_list,s=1)

# 重绘制起点和终点
# plt.scatter(rw.x_list[0], rw.y_list[0], s=100, c='red')
# plt.scatter(rw.x_list[-1], rw.y_list[-1], s=100, c='yellow')

# 隐藏坐标轴
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)

#屏幕尺寸
# plt.figure(figsize=(10,6),dpi=128)
plt.show()
