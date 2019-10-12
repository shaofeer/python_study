"""
给定5 输出：
01  16  15  14  13
02  17  24  23  12
03  18  25  22  11
04  19  20  21  10
05  06  07  08  09

向下走：(0,0)(1,0)(2,0)(3,0)(4,0)
向右走：(4,1)(4,2)(4,3)
向上走：(3,3)(3,2)(3,1)
向左走：(2,1)(1,1)(0,1)
"""

num = 5
result_arr = []

for i in range(num):
    result_arr.append([0] * num)

# row 代表 行
row = 0
# col 代表 列
col = 0

# r 代表方向 U D L R
r = 'D'

for i in range(1, num * num + 1):
    result_arr[row][col] = i

    # 左下角转弯和右上角转弯
    if row + col == num - 1:
        if row < col:
            r = 'L'
        else:
            r = "R"

    # 右下
    if row == col and col >= num / 2:
        r = 'U'
    # 左上
    if col - row == 1 and col <= num / 2:
        r = 'D'

    if r == "U":
        row -= 1
    if r == 'D':
        row += 1
    if r == 'L':
        col -= 1
    if r == 'R':
        col += 1

for i in range(num):
    for j in range(num):
        print("%02d  " % result_arr[i][j], end='')
    print()
