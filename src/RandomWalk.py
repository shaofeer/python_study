from random import choice


class RandomWalk:
    """生成随机漫步的类"""

    def __init__(self, step_num=5000):
        # 需要走的总步数
        self.step_num = step_num
        # 所经过的x点 默认从原点起步
        self.x_list = [0]
        # 所经过的y点 默认从原点起步
        self.y_list = [0]

    def fill_walk(self):
        # 产生随机点
        while len(self.x_list) < self.step_num:
            # 小于总步数
            # 计算前进方向和前进距离 1代表左移动，-1右移
            x_direction = choice([1, -1])
            # 移动距离范围 如果为0 那么是上下移动
            x_distance = choice([0, 1, 2, 3, 4, 5])
            # 计算移动距离
            x_step = x_direction * x_distance

            # 计算前进方向和前进距离 1代表上移动，-1下移
            y_direction = choice([1, -1])
            # 移动距离范围 如果为0 那么是上下移动
            y_distance = choice([0, 3, 4, 5 ])
            # 计算移动距离
            y_step = y_direction * y_distance

            # 杜绝原地不动
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的坐标
            x_next_step = self.x_list[-1] + x_step
            y_next_step = self.y_list[-1] + y_step

            # 记录距离
            self.x_list.append(x_next_step)
            self.y_list.append(y_next_step)
