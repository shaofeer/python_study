import csv
from matplotlib import pyplot as plt
from datetime import datetime

dates = []
datas = []

with open('data.csv', 'r') as cf:
    reader = csv.reader(cf)

    for data in reader:
        dates.append(datetime.strptime(data[0], '%Y-%m-%d'))
        datas.append(int(data[1]))

plt.plot(dates, datas)
plt.show()
