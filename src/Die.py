from random import randint


class Die:
    def __init__(self, num_sides=6):
        """默认为6面骰子"""
        self.num_sides = num_sides

    def roll(self):
        """生成一个从1到指定骰子的面一个随机数"""
        return randint(1, self.num_sides)
