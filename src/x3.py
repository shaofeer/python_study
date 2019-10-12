import matplotlib.pyplot as plt

x_v = range(5000)
# x_v = [1, 2, 3, 4, 5]
y_v = [x * x * x for x in x_v]

plt.scatter(x_v, y_v, s=4, cmap=plt.cm.Reds, c=y_v, edgecolors=None)
plt.show()
