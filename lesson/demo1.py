"""
给定4 输出：
01  12  11  10
02  13  16  09
03  14  15  08
04  05  06  07
"""

num = 7

result_arr = [[0] * num]

for item in range(num - 1):
    result_arr += [[0] * num]

# i ==> 行索引  j ==> 列索引
i = j = 0
# r 控制方向  r = 1 向下 r = 2 向右 r = 3 向上 r = 4 向左
r = 1
# 填充数据
for ii in range(1, num * num + 1):
    result_arr[i][j] = ii

    # 左下角或右上角的数
    if i + j == num - 1:
        if i > j:
            # 在左下角
            r = 2
        else:
            # 在右上角
            r = 4

    elif i == j and j >= num / 2:
        # 在右下角
        r = 3

    elif i - j == -1 and j <= num / 2:
        # 在左上角
        r = 1

    # 根据方向来设置索引的变化
    if r == 1:
        i += 1
    elif r == 2:
        j += 1
    elif r == 3:
        i -= 1
    elif r == 4:
        j -= 1

for i in range(num):
    for j in range(num):
        print("%02d  " % result_arr[i][j], end='')
    print()
