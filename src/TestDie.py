from src.Die import Die
import pygal

die = Die()

result = []

for i in range(100):
    num = die.roll()
    result.append(num)

# print(result)

# 分析每个点出现了几次
fre_res = []
for i in range(1, die.num_sides + 1):
    fre_res.append(result.count(i))

print(fre_res)

bar = pygal.Bar()

bar._title = '骰子'
bar.x_labels = range(1, die.num_sides + 1)
bar.y_labels = fre_res

bar.add(title='D6', values=fre_res)
bar.render_to_file("aaa.svg")
